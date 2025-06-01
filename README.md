# Sistema-Experto-para-la-Deteccion-de-Estres-Laboral
El proyecto consiste en el diseño e implementación de un Sistema Experto para la identificación temprana y manejo del estrés laboral.
## Descripción
Este proyecto implementa un sistema experto sencillo en Python que evalúa un conjunto de reglas basadas en hechos de entrada y devuelve inferencias. La API está desarrollada con FastAPI para exponer un endpoint `/api/inferir` que recibe datos en JSON y responde con los resultados del motor de inferencia.

## Estructura del repositorio

```markdown
Sistema-Experto-para-la-Deteccion-de-Estres-Laboral/
│
├── docs/ # Documentación en PDF
│ └── manual_sistema_experto.pdf
│
├── expert_system/ # Lógica del sistema experto
│ ├── init.py
│ ├── engine.py # Motor de inferencia
│ └── reglas.py # Definición de reglas
│
├── app/ # API con FastAPI
│ ├── init.py
│ ├── main.py # Punto de entrada de la API
│ ├── schemas.py # Modelos Pydantic (entradas/salidas)
│ └── routes.py # Endpoints REST
│
├── tests/ # Pruebas unitarias
│ ├── init.py
│ ├── test_engine.py
│ └── test_api.py
│
├── requerimientos.txt # Dependencias del proyecto
└── README.md # Esta guía

## Requisitos e instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/arytdf/Sistema-Experto-para-la-Deteccion-de-Estres-Laboral
   cd mi_sistema_experto

## (Opcional) Crea y activa un entorno virtual:
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate

## Instala las dependencias:
pip install -r requerimientos.txt

## Cómo ejecutar la API
Para iniciar el servidor en modo desarrollo, ejecuta:

uvicorn app.main:app --reload

Por defecto, la API estará disponible en http://localhost:8000. Puedes ver la documentación interactiva de Swagger en http://localhost:8000/docs.

## Uso de la API (ejemplo)
Envía una petición POST a /api/inferir con un JSON como este:

{
  "temperatura": 35,
  "humedad": 70
}

Respuesta esperada:

{
  "hechos": {
    "temperatura": 35,
    "humedad": 70,
    "recomendacion": "Hace mucho calor, activar aire acondicionado"
  }
}

Ajusta los campos de entrada según las variables que definas en tu sistema experto.

## Documentación detallada
Para más información sobre la lógica interna, el motor de inferencia, las reglas implementadas y ejemplos de casos de uso, descarga y consulta el PDF en:

docs/manual_sistema_experto.pdf

## Estructura del sistema experto
expert_system/engine.py: Motor de inferencia que recorre las reglas definidas y genera nuevos hechos a partir de los datos de entrada.

expert_system/rules.py: Conjunto de reglas representadas como funciones de antecedentes y conclusiones.

app/schemas.py: Modelos Pydantic para validar y serializar la entrada y salida de datos.

app/routes.py: Rutas de FastAPI que exponen el endpoint /api/inferir y llaman al motor de inferencia.

tests/: Pruebas unitarias para verificar que el motor de inferencia y los endpoints funcionan correctamente.

## Ejecutar pruebas
Si deseas comprobar que todo funciona correctamente, instala pytest (si no está ya en requirements.txt) y ejecuta:

pytest

Los archivos de prueba se encuentran en tests/test_engine.py y tests/test_api.py.

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles (si decides agregar uno).

## Autores y contacto
Autor: Ariel M. Altamirano

Correo: arytdf@gmail.com

Si encuentras algún error o tienes sugerencias, abre un issue en GitHub o envía un correo a la dirección indicada.


