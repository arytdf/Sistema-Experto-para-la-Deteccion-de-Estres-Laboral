# app.py
import streamlit as st
import json
from pathlib import Path
from functools import partial
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# ───── Configuración inicial ──────────────────────────────────
st.set_page_config(
    page_title="Test de Estrés Laboral",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="collapsed"
)
BASE = Path(__file__).parent

# ───── Carga de estilos ───────────────────────────────────────
with open(BASE / "styles.css", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ───── Carga de datos ───────────────────────────────
with open(BASE / "data/reglas.json", encoding="utf-8") as f:
    reglas_data = json.load(f)
    # Crear diccionario de reglas
    REGLAS = {}
    for item in reglas_data.get('entries', []):
        REGLAS[item['name']] = item['props']

with open(BASE / "data/diagnosticos.json", encoding="utf-8") as f:
    diag_data = json.load(f)
    # Crear diccionario de diagnósticos
    DIAG = {}
    for item in diag_data.get('entries', []):
        # Unir lista QUE_HACER con saltos de línea
        if 'QUE_HACER' in item['props'] and isinstance(item['props']['QUE_HACER'], list):
            item['props']['QUE_HACER'] = "\n".join(item['props']['QUE_HACER'])
        DIAG[item['name']] = item['props']

# Asegurar que los nodos de diagnóstico estén en REGLAS
for key in DIAG.keys():
    if key not in REGLAS:
        REGLAS[key] = DIAG[key]

# ───── Estado de sesión ────────────────────────────────────────
DEFAULT_STATE = {"pagina": "inicio", "nodo_actual": "B", "historial": [], "respuestas": []}
for key, val in DEFAULT_STATE.items():
    st.session_state.setdefault(key, val)

# ───── Funciones ───────────────────────────────────────────────
def comenzar_test():
    st.session_state.pagina = "preguntas"

def retroceder():
    st.session_state.nodo_actual = st.session_state.historial.pop()

def avanzar(resp: str):
    nodo = REGLAS[st.session_state.nodo_actual]
    st.session_state.respuestas.append((nodo["PREGUNTA"], resp))
    st.session_state.historial.append(st.session_state.nodo_actual)
    st.session_state.nodo_actual = nodo["RESPUESTAS"][resp]

def reiniciar_test():
    st.session_state.update(DEFAULT_STATE)

def finalizar_test():
    st.session_state.pagina = "despedida"

def generar_pdf() -> bytes:
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    w, h = A4
    x, y = 40, h - 40

    pdf.setTitle("Informe – Test de Estrés Laboral")
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(x, y, "Informe – Test de Estrés Laboral")
    y -= 32

    diag = DIAG[st.session_state.nodo_actual]
    pdf.setFont("Helvetica", 12)
    pdf.drawString(x, y, f"Diagnóstico final: {diag['DIAGNOSTICO']}")
    y -= 26

    pdf.drawString(x, y, "Respuestas:")
    y -= 20
    pdf.setFont("Helvetica", 11)
    for i, (preg, resp) in enumerate(st.session_state.respuestas, 1):
        pdf.drawString(x + 10, y, f"{i}. {preg} → {resp}")
        y -= 14
        if y < 60:
            pdf.showPage()
            y = h - 40
            pdf.setFont("Helvetica", 11)

    pdf.save()
    buffer.seek(0)
    return buffer.getvalue()

# ───── Interfaz ────────────────────────────────────────────────
pagina = st.session_state.pagina

# 1) Pantalla de bienvenida
if pagina == "inicio":
    st.markdown('<div class="header-test"><h1>¡Bienvenido/a!</h1></div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="welcome-box">
          <p>
            Bienvenido/a al Test de Estrés Laboral. A través de preguntas breves,
            identificarás tu nivel de estrés laboral, sus posibles causas y obtendrás recomendaciones.
            Presiona <strong>COMENZAR TEST</strong> y responde SÍ o NO.
          </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    cols = st.columns([1, 4, 1], gap="small")
    cols[1].button("COMENZAR TEST", key="btn_comenzar", use_container_width=True, on_click=comenzar_test)

# 2) Preguntas
elif pagina == "preguntas":
    st.markdown('<div class="header-test"><h1>TEST DE ESTRÉS LABORAL</h1></div>', unsafe_allow_html=True)
    nodo = REGLAS[st.session_state.nodo_actual]
    if "PREGUNTA" in nodo:
        st.markdown(f'<div class="box-pregunta"><strong>{nodo["PREGUNTA"]}</strong></div>', unsafe_allow_html=True)
        if st.session_state.historial:
            cols = st.columns([1, 3, 3, 3, 1], gap="small")
            cols[1].button("ANTERIOR", key="btn_ant", use_container_width=True, on_click=retroceder)
            cols[2].button("SÍ", key="btn_si", use_container_width=True, on_click=partial(avanzar, "SI"))
            cols[3].button("NO", key="btn_no", use_container_width=True, on_click=partial(avanzar, "NO"))
        else:
            _, c_si, c_no, _ = st.columns([1, 4, 4, 1], gap="small")
            c_si.button("SÍ", key="btn_si0", use_container_width=True, on_click=partial(avanzar, "SI"))
            c_no.button("NO", key="btn_no0", use_container_width=True, on_click=partial(avanzar, "NO"))
    else:
        st.session_state.pagina = "diagnostico"
        st.rerun()

# 3) Diagnóstico
elif pagina == "diagnostico":
    st.markdown('<div class="header-test"><h1>TEST DE ESTRÉS LABORAL</h1></div>', unsafe_allow_html=True)
    diag = DIAG[st.session_state.nodo_actual]
    que_html = diag["QUE_HACER"].replace("\n", "<br/>")
    st.markdown(
        f"""
        <div class="diag-box">
          <h3>{diag['DIAGNOSTICO']}</h3>
          <p>{diag['RECOMENDACION']}</p>
          <h5>¿Qué hacer?</h5>
          <p>{que_html}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    cols = st.columns([1, 4, 4, 1], gap="small")
    cols[1].button("REINICIAR", key="btn_rein", use_container_width=True, on_click=reiniciar_test)
    cols[2].button("FINALIZAR", key="btn_fin", use_container_width=True, on_click=finalizar_test)

# 4) Despedida
else:
    st.markdown('<div class="header-test"><h1>¡Gracias por realizar el test!</h1></div>', unsafe_allow_html=True)
    st.success("Podés descargar tu informe en PDF o volver a comenzar cuando quieras.")
    cols = st.columns([1, 4, 4, 1], gap="small")
    cols[1].download_button("DESCARGAR INFORME EN PDF", data=generar_pdf(), file_name="informe_estres_laboral.pdf", mime="application/pdf", key="btn_pdf", use_container_width=True)
    cols[2].button("REALIZAR NUEVAMENTE", key="btn_new", use_container_width=True, on_click=reiniciar_test)