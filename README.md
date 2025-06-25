# Sistema Experto para la Detección de Estrés Laboral en Tierra del Fuego

Este proyecto implementa un **Sistema Experto** para la detección temprana de estrés laboral, desarrollado en *Python* con **Streamlit**.  
Se apoya en un árbol de decisión clínico validado por especialistas para evaluar síntomas físicos, emocionales y factores laborales, generando un **diagnóstico personalizado** con recomendaciones y un **informe PDF** descargable.

Desarrollado como proyecto académico para el *Politécnico Malvinas Argentinas* bajo la dirección del **Prof. Martín Mirabete**.

---

## 🌐 Demo en Vivo

[Acceda a la aplicación desplegada en Streamlit Cloud](https://sistema-experto-para-la-deteccion-de-estres-laboral.streamlit.app/)

---

## 🔍 Características Principales

- **Cuestionario interactivo**: flujo adaptativo de preguntas **SÍ / NO** con navegación **AVANZAR** y **VOLVER**.  
- **Diagnóstico por niveles de riesgo**:  
  - 🔴 **Alto** – intervención urgente.  
  - 🟠 **Moderado** – acciones correctivas.  
  - 🟡 **Leve** – monitoreo y recomendaciones.  
  - 🟢 **Bajo** – refuerzo positivo.  
- **Informe clínico en PDF**: descarga personalizada con resultados y recomendaciones.  
- **Arquitectura modular**: separación entre motor de inferencia e interfaz.  
- **Base de conocimiento validada**: por la psicóloga **Micaela Barria**, especialista en estrés laboral.  
- **Diseño *responsive***: experiencia óptima en escritorio y móviles.  

---

## ⚙️ Tecnologías Utilizadas

| Componente            | Tecnología                  | Función                                    |
|-----------------------|-----------------------------|--------------------------------------------|
| Front‑end             | **Streamlit**               | Interfaz web interactiva                   |
| Back‑end              | **Python&nbsp;3.10**        | Lógica de la aplicación                    |
| Motor de inferencia   | **JSON + Forward Chaining** | Procesamiento de reglas                    |
| Generación de PDF     | **ReportLab + PyPDF2**      | Creación de informes                       |
| Gestión de reglas     | **YAML / JSON**             | Base de conocimiento                       |
| Despliegue            | **Streamlit Community Cloud** | Hosting gratuito en la nube               |

---

## 📁 Estructura del Proyecto
```text
/Sistema-Experto-para-la-Deteccion-de-Estres-Laboral/
│
├── app.py                # Lógica principal de la app Streamlit
├── styles.css            # Estilos personalizados
├── requirements.txt      # Dependencias Python
├── sistema_experto.bat   # Script Windows para setup y ejecución
├── .gitignore            # Exclusiones de Git
├── data/                 # Datos y recursos
│   ├── convert_yml_to_json.bat  # Conversor YAML → JSON (Windows)
│   ├── reglas.yml        # Árbol de reglas (editable)
│   ├── generate_json.py  # Script de conversión YAML → JSON
│   ├── reglas.json       # Reglas en JSON para la app
│   └── diagnosticos.json # Mensajes de diagnóstico
└── documentos/           # Documentación adicional
    ├── Descripción detallada del proyecto.pdf
    ├── Diagrama SE con identificación de nodos.png
    └── Representación y Organización del conocimiento.pdf
```

---

## 🗂️ Base de Conocimiento

El sistema se basa en reglas *if‑then* fundamentadas en:

- **Modelo de Karasek** (carga laboral vs. control).  
- **Inventario de Burnout de Maslach**.  
- **Guías de la OMS** para manejo del estrés.  
- Criterios clínicos validados por la **Psic. Micaela Barria**.  

### Clasificación de Riesgo

| Nivel      | Color | Acción recomendada            |
|------------|-------|-------------------------------|
| Alto       | 🔴    | Intervención urgente          |
| Moderado   | 🟠    | Acciones correctivas          |
| Leve       | 🟡    | Monitoreo y prevención        |
| Bajo       | 🟢    | Refuerzo positivo             |

---

## 🚀 Instalación y Ejecución

### Prerrequisitos
- **Python 3.10** o superior  
- **Git** (opcional)  

### Pasos para ejecutar localmente
```bash
# 1. Clonar repositorio
git clone https://github.com/arvtdf/Sistema-Experto-para-la-Deteccion-de-Estres-Laboral.git
cd Sistema-Experto-para-la-Deteccion-de-Estres-Laboral

# 2. Crear y activar entorno virtual
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. (Opcional) Convertir reglas YAML → JSON si modificaste reglas.yml
python -c "import yaml, json; data = yaml.safe_load(open('data/reglas.yml')); open('data/reglas.json','w').write(json.dumps(data, indent=2))"

# 5. Ejecutar aplicación
streamlit run app.py
```

### Ejecución rápida en Windows
```cmd
sistema_experto.bat
```

---

## 📡 Uso en Línea

La aplicación está disponible 24/7 en:  
<https://sistema-experto-para-la-deteccion-de-estres-laboral.streamlit.app/>

Flujo principal del usuario:

1. **Pantalla inicial** – explicación del test y consentimiento informado.  
2. **Cuestionario adaptativo** – 10‑15 preguntas SÍ/NO con navegación bidireccional.  
3. **Diagnóstico personalizado** – nivel de riesgo y explicación.  
4. **Generación de PDF** – informe completo con recomendaciones.  
5. **Pantalla final** – opción para reiniciar el test o compartir resultados.  

---

## 💡 ¿Por qué Streamlit?

- **Desarrollo rápido**: Apps web interactivas con solo Python.  
- **Interactividad nativa**: Widgets integrados; sin JavaScript.  
- **Arquitectura SPA**: *Single‑Page Application* ideal para flujos secuenciales.  
- **Despliegue sin servidores**: Publicación en la nube con un clic.  
- **Separación de preocupaciones**: Lógica y presentación limpias.  

### Alternativas consideradas
- **Flask / FastAPI** – requirieron más desarrollo front‑end.  
- **Gradio** – menor flexibilidad para flujos complejos.  
- **Apps nativas** – mayor complejidad de distribución.  

---

## 👩‍⚕️ Aporte Clínico

El conocimiento experto validado por la **Psic. Micaela Barria** garantiza:

- Detección temprana de síntomas físicos y emocionales.  
- Evaluación de factores laborales críticos (horas extra, autonomía, apoyo).  
- Estrategias de mitigación personalizadas.  
- Prevención de *burnout* y ausentismo laboral.  

---

## 📄 Licencia

Distribuido bajo licencia **MIT**. Consulta el archivo `LICENSE` para más detalles.

---

## ✍️ Autor

**Ariel Martín Altamirano**  
Desarrollo de Sistemas de IA – 2025  
Universidad Nacional de Tierra del Fuego  












