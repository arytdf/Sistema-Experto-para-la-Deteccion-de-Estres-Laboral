# Sistema Experto para la Detección de Estrés Laboral en Tierra del Fuego

Este proyecto implementa un **Sistema Experto** para la detección temprana de estrés laboral, desarrollado en *Python* con **Streamlit**.  
Se apoya en un árbol de decisión clínico validado por especialistas para evaluar síntomas físicos, emocionales y factores laborales, generando un **diagnóstico personalizado** con recomendaciones específicas para **prevenir el burnout, reducir el ausentismo laboral y mejorar el bienestar psicológico**.

Desarrollado como proyecto académico para el *Politécnico Malvinas Argentinas* bajo la dirección del **Prof. Martín Mirabete**.

📁 **Repositorio GitHub:** [https://github.com/arvtdf/Sistema-Experto-para-la-Deteccion-de-Estres-Laboral](https://github.com/arvtdf/Sistema-Experto-para-la-Deteccion-de-Estres-Laboral)

---

## 🌐 Demo en Vivo

[Acceder a la aplicación en Streamlit Cloud](https://sistema-experto-para-la-deteccion-de-estres-laboral.streamlit.app/)

---

## 🔍 Características del Sistema

- **Cuestionario adaptativo**: flujo de preguntas tipo árbol de decisión (Sí/No y opciones múltiples).
- **Diagnóstico por niveles de riesgo**:  
  - 🔴 **Alto** – intervención urgente.  
  - 🟠 **Moderado** – acciones correctivas.  
  - 🟡 **Leve** – monitoreo y recomendaciones.  
  - 🟢 **Bajo** – refuerzo positivo.  
- **Motor de inferencia forward chaining**: razonamiento automático sobre hechos ingresados.
- **Informe en PDF**: diagnóstico y plan de acción personalizado descargable.
- **Diseño *responsive***: funcional en computadoras, tablets y móviles.
- **Base clínica validada**: conocimiento estructurado junto a la psicóloga **Micaela Barria**.

---

## ⚙️ Tecnologías Utilizadas

| Componente            | Tecnología                  | Función                                    |
|-----------------------|-----------------------------|--------------------------------------------|
| Interfaz              | **Streamlit**               | Web interactiva                            |
| Lógica                | **Python 3.10**             | Back-end y motor                           |
| Inferencia            | **JSON + Forward Chaining** | Reglas tipo If-Then                        |
| Informes              | **ReportLab + PyPDF2**      | Generación de PDF                          |
| Despliegue            | **Streamlit Cloud**         | Hosting gratuito                           |

---

## 📁 Estructura del Proyecto

```text
/Sistema-Experto-para-la-Deteccion-de-Estres-Laboral/
│
├── app.py                 # Aplicación principal Streamlit
├── estilos.css            # Estilos personalizados
├── requirements.txt       # Dependencias
├── sistema_experto.bat    # Script de automatización Windows
├── /core/
│   ├── motor.py           # Motor de inferencia
│   └── carga_base.py      # Carga del conocimiento
├── /servicios/
│   └── generador_reporte.py # Informe PDF
├── /data/
│   └── base.json          # Síntomas, reglas y diagnósticos
└── /documentos/
    └── Representación y Organización del conocimiento.pdf
```

---

## 🚀 Instalación y Ejecución

### Requisitos
- Python 3.10 o superior
- Git (opcional)

### Pasos para ejecutar localmente

```bash
# 1. Clonar el repositorio
git clone https://github.com/arvtdf/Sistema-Experto-para-la-Deteccion-de-Estres-Laboral.git
cd Sistema-Experto-para-la-Deteccion-de-Estres-Laboral

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno
# Windows:
venv\Scripts\activate
# Linux / macOS:
source venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar aplicación
streamlit run app.py
```

### Alternativa rápida (Windows)
```cmd
sistema_experto.bat
```

---

## 🧭 Flujo de Usuario

1. **Pantalla inicial**: bienvenida y explicación.
2. **Evaluación**: entre 10 y 12 preguntas según las respuestas.
3. **Diagnóstico**: evaluación personalizada del nivel de riesgo.
4. **Informe**: opción de descargar PDF con plan de acción.
5. **Pantalla final**: reiniciar evaluación o finalizar.

---

## 👩‍⚕️ Aporte Profesional

La psicóloga **Micaela Barria**, especialista en estrés laboral, participó en la validación del conocimiento, incluyendo:

- Priorización de síntomas críticos.
- Evaluación de factores organizacionales.
- Estrategias de mitigación individual y organizacional.
- Prevención de *burnout* y ausentismo laboral.

> “Un sistema experto bien diseñado puede complementar el juicio clínico, pero nunca reemplazarlo” – Psic. M. Barria

---

## 📄 Licencia

Distribuido bajo licencia **MIT**. Consultar el archivo `LICENSE` para más información.

---

## ✍️ Autor

**Ariel Martín Altamirano**  
Desarrollo de Sistemas de IA – 2025  
Politécnico Malvinas Argentinas - Rio Grande - Tierra del Fuego














