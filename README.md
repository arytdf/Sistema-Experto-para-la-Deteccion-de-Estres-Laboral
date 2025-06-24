# Test de Estrés Laboral

Este proyecto es una aplicación de Streamlit que permite evaluar el nivel de estrés laboral mediante un breve cuestionario de preguntas SÍ/NO, genera un diagnóstico y ofrece la opción de descargar un informe en PDF.

## Características

- Pantalla de bienvenida con instrucciones.
- Flujo de preguntas (árbol de decisión) con navegación ANTERIOR.
- Pantalla de diagnóstico con recomendaciones.
- Descarga de informe final en PDF.
- Pantalla de despedida con opción de reiniciar el test.

## Estructura del proyecto

```
/SistemaExperto/
│
├── app.py               # Lógica principal de la app Streamlit
├── styles.css           # Estilos personalizados en CSS
├── requirements.txt     # Dependencias Python del proyecto
├── sistema_experto.bat  # Script de Windows para setup y ejecución
├── .gitignore           # Archivos y carpetas excluidas del repositorio
├── data/                # Datos de entrada y recursos
│   ├── reglas.yml       # Definición del árbol de reglas en YAML
│   ├── reglas.json      # Regenerado desde reglas.yml para consumo de la app
│   └── diagnosticos.json# Mensajes y recomendaciones finales
└── documentos/          # Documentación y manuales adicionales
    └── ManualUsuario.md # Guía de uso para el usuario
```

## Instalación

Clona el repositorio o descárgalo como ZIP:

```bash
git clone <URL_DEL_REPOSITORIO>
cd SistemaExperto
```

### Creación de entorno virtual (recomendado)

Es importante usar un entorno virtual aislado para gestionar dependencias:

```bash
# Windows
python -m venv venv
venv\\Scripts\\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Instalación de dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> **Sugerencia:** en Windows, ejecuta `sistema_experto.bat` para automatizar estos pasos, incluida la instalación de PyYAML necesaria para convertir archivos YAML a JSON.

## Uso

```bash
streamlit run app.py
```

La aplicación abrirá en tu navegador predeterminado.

## Archivo YAML a JSON

En el proyecto, las reglas y diagnósticos pueden definirse en formato YAML para facilitar la edición. Utiliza PyYAML para convertirlos a JSON:

```bash
python - << 'EOF'
import yaml, json
with open('data/reglas.yml', encoding='utf-8') as yf:
    data = yaml.safe_load(yf)
with open('data/reglas.json', 'w', encoding='utf-8') as jf:
    json.dump(data, jf, ensure_ascii=False, indent=2)
EOF
```

## Licencia

MIT License
```
