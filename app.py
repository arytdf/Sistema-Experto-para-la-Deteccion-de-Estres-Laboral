import sys
import subprocess
import os

# Verificar e instalar dependencias faltantes solo en Streamlit Cloud
if "streamlit" in sys.modules:
    required = {"reportlab", "PyPDF2", "python-dotenv"}
    try:
        installed_output = subprocess.check_output([sys.executable, "-m", "pip", "freeze"]).decode()
        installed = {pkg.split("==")[0] for pkg in installed_output.split("\n") if pkg}
        missing = required - installed

        if missing:
            print(f"Instalando paquetes faltantes: {', '.join(missing)}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])
    except Exception as e:
        print(f"Error verificando dependencias: {str(e)}")

import streamlit as st
from core.carga_base import CargaBase
from core.motor import MotorInferencia
from servicios.generador_reporte import generar_pdf
import datetime

# Configuración de página
st.set_page_config(
    page_title="Sistema Experto - Estrés Laboral",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Cargar estilos CSS
def cargar_estilos():
    try:
        with open("estilos.css", "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("No se encontró el archivo de estilos CSS")

cargar_estilos()

# Estado de la sesión
ESTADO_INICIAL = {
    "pagina": "inicio",
    "motor": None,
    "respuestas": [],
    "sintoma_actual": None,
    "progreso": 0
}

if 'pagina' not in st.session_state:
    st.session_state.update(ESTADO_INICIAL)

# Funciones de navegación
def comenzar_evaluacion():
    try:
        base = CargaBase("data/base.json")
        st.session_state.pagina = "preguntas"
        st.session_state.motor = MotorInferencia(base.datos)
        st.session_state.sintoma_actual = None
        st.session_state.respuestas = []
        st.session_state.progreso = 0
    except Exception as e:
        st.error(f"Error al iniciar la evaluación: {str(e)}")
        st.session_state.pagina = "inicio"

def manejar_respuesta(respuesta):
    try:
        motor = st.session_state.motor
        sintoma = st.session_state.sintoma_actual
        
        if not sintoma:
            st.session_state.pagina = "diagnostico"
            return
            
        if isinstance(respuesta, bool):
            hecho = sintoma["id"] if respuesta else f"!{sintoma['id']}"
            respuesta_str = "Sí" if respuesta else "No"
        else:
            hecho = f"{sintoma['id']}:{respuesta}"
            respuesta_str = sintoma["opciones"][respuesta]
        
        st.session_state.respuestas.append((sintoma["pregunta"], respuesta_str))
        st.session_state.progreso = min(100, st.session_state.progreso + (100 // len(motor.sintomas)))
        motor.agregar_hecho(hecho)
        st.session_state.sintoma_actual = motor.obtener_proximo_sintoma()
        
        if motor.diagnostico_actual is not None or st.session_state.sintoma_actual is None:
            st.session_state.pagina = "diagnostico"
    except Exception as e:
        st.error(f"Error al procesar respuesta: {str(e)}")
        st.session_state.pagina = "inicio"

def reiniciar_evaluacion():
    st.session_state.update(ESTADO_INICIAL)

def finalizar_evaluacion():
    st.session_state.pagina = "despedida"

# Interfaz de usuario
if st.session_state.pagina == "inicio":
    # Encabezado con estilo similar a la imagen
    st.markdown(
        """
        <div style="
            background-color: #d1ecd1;
            padding: 30px;
            border-radius: 12px 12px 0 0;
            text-align: center;
            margin-bottom: 0;
        ">
            <h1 style="color: #111827; margin: 0;">¡Bienvenido/a!</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Caja de bienvenida 
    st.markdown(
        """
        <div style="
            background-color: #f3f4f6;
            border-radius: 0 0 12px 12px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            text-align: center;
        ">
            <p style="font-size: 1.1rem; color: #111827; line-height: 1.6;">
                Bienvenido/a al Test de Estrés Laboral. A través de preguntas breves,
                identificarás tu nivel de estrés laboral, sus posibles causas y obtendrás recomendaciones.
            </p>
            <p style="font-size: 1.1rem; color: #111827; line-height: 1.6;">
                Presiona <strong>COMENZAR TEST</strong> y responde SÍ o NO.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Botón centrado y con estilo
    cols = st.columns([1, 3, 1])
    with cols[1]:
        st.button(
            "COMENZAR TEST", 
            on_click=comenzar_evaluacion, 
            use_container_width=True,
            key="comenzar_test"
        )

elif st.session_state.pagina == "preguntas":
    st.markdown('<div class="header-test"><h1>Evaluación de Estrés Laboral</h1></div>', unsafe_allow_html=True)
    
    if st.session_state.motor is None:
        base = CargaBase("data/base.json")
        st.session_state.motor = MotorInferencia(base.datos)
    
    if st.session_state.sintoma_actual is None:
        st.session_state.sintoma_actual = st.session_state.motor.obtener_proximo_sintoma()
    
    sintoma = st.session_state.sintoma_actual
    
    if sintoma:
        st.progress(st.session_state.progreso / 100)
        st.caption(f"Progreso: {st.session_state.progreso}%")
        
        st.markdown(f'<div class="question-box"><strong>{sintoma["pregunta"]}</strong></div>', unsafe_allow_html=True)
        
        if "explicacion" in sintoma:
            with st.expander("ℹ️ Más información", expanded=False):
                st.info(sintoma["explicacion"])
        
        if "opciones" in sintoma:
            opciones = list(sintoma["opciones"].items())
            cols = st.columns(len(opciones))
            for i, (key, value) in enumerate(opciones):
                cols[i].button(value, on_click=manejar_respuesta, args=(key,), use_container_width=True)
        else:
            cols = st.columns([1, 1, 1])
            cols[0].button("SÍ", on_click=manejar_respuesta, args=(True,), use_container_width=True)
            cols[2].button("NO", on_click=manejar_respuesta, args=(False,), use_container_width=True)
    else:
        st.session_state.pagina = "diagnostico"
        st.rerun()

elif st.session_state.pagina == "diagnostico":
    st.markdown('<div class="header-test"><h1>Resultado de la Evaluación</h1></div>', unsafe_allow_html=True)
    
    motor = st.session_state.motor
    
    if motor is None or not hasattr(motor, 'diagnosticos'):
        st.error("Error: No se pudo cargar la información de diagnóstico")
        st.button("Volver al inicio", on_click=reiniciar_evaluacion)
        st.stop()
    
    clave_diag = motor.diagnostico_actual or "CA"
    diagnostico = motor.diagnosticos.get(clave_diag, motor.diagnosticos.get("CA", {}))
    
    # Asignar clase CSS según severidad
    clase_severidad = ""
    if "🔴" in diagnostico.get("DIAGNOSTICO", ""):
        clase_severidad = "high-severity"
    elif "🟠" in diagnostico.get("DIAGNOSTICO", ""):
        clase_severidad = "medium-high-severity"
    elif "🟡" in diagnostico.get("DIAGNOSTICO", ""):
        clase_severidad = "medium-severity"
    elif "🟢" in diagnostico.get("DIAGNOSTICO", ""):
        clase_severidad = "low-severity"
    
    st.markdown(
        f"""
        <div class="diagnosis-box {clase_severidad}">
            <h3>{diagnostico.get('DIAGNOSTICO', 'Diagnóstico no disponible')}</h3>
            <p><strong>Nivel de riesgo:</strong> {diagnostico.get('RIESGO', 'No especificado')}</p>
            <p><strong>Recomendación principal:</strong> {diagnostico.get('RECOMENDACION', '')}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    with st.expander("🔍 Plan de acción detallado", expanded=True):
        plan_accion = diagnostico.get('QUE_HACER', 'Plan de acción no disponible').replace('\n', '<br/>')
        st.markdown(
            f"""
            <div class="action-plan">
                <p>{plan_accion}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    st.markdown("---")
    st.subheader("Recursos de apoyo")
    st.markdown("""
    - **Línea de ayuda psicológica:** 0800-999-0091 (Argentina). Funcionando las 24 horas los 365 días del año
    - **Salud Mental:** 2964-422285 (Río Grande). Horario de atención de lunes a viernes de 8 a 17 hs.          
    - **Guía OMS para manejo de estrés:** [Descargar PDF](https://www.who.int/docs/default-source/mental-health/sh-2020-spa-3-web.pdf)
    - **Ejercicios de respiración guiada:** [Video tutorial](https://youtu.be/tYwnSBkc_To)
    """)
    
    col1, col2 = st.columns(2)
    col1.button("REINICIAR EVALUACIÓN", on_click=reiniciar_evaluacion, use_container_width=True)
    col2.button("DESCARGAR INFORME", on_click=finalizar_evaluacion, use_container_width=True)

elif st.session_state.pagina == "despedida":
    st.markdown('<div class="header-test"><h1>¡Gracias por completar la evaluación!</h1></div>', unsafe_allow_html=True)
    st.success("""
    Tu informe detallado está listo para descargar. Contiene:
    
    - Diagnóstico completo
    - Análisis de tus respuestas
    - Plan de acción personalizado
    - Recursos científicos de apoyo
    """)
    
    # Generar PDF
    try:
        motor = st.session_state.motor
        clave_diag = motor.diagnostico_actual or "CA"
        
        pdf_file = generar_pdf(
            st.session_state.respuestas,
            clave_diag,
            motor.diagnosticos
        )
        
        st.download_button(
            "⬇️ DESCARGAR INFORME COMPLETO EN PDF",
            data=pdf_file,
            file_name=f"informe_estres_laboral_{datetime.datetime.now().strftime('%Y%m%d')}.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    except Exception as e:
        st.error(f"Error al generar el informe: {str(e)}")
    
    st.button("REALIZAR NUEVA EVALUACIÓN", on_click=reiniciar_evaluacion, use_container_width=True)

# Pie de página
st.markdown("---")
st.caption("Sistema Experto para Evaluación de Estrés Laboral - © 2025")