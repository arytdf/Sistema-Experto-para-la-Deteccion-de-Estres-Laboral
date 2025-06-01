# app/schemas.py

from pydantic import BaseModel
from typing import Dict, Any

class ContextoEntrada(BaseModel):
    # Campos que el cliente enviará para describir el estado inicial
    temperatura: int
    humedad: int
    # …otros campos que tu sistema experto necesite

class ResultadoSalida(BaseModel):
    # Puedes retornar todos los hechos finales o solo la conclusión
    hechos: Dict[str, Any]
    # Por ejemplo: {"temperatura": 35, "recomendacion": "…"}
