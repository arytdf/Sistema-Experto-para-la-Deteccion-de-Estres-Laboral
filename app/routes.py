# app/routes.py

from fastapi import APIRouter, HTTPException
from app.schemas import ContextoEntrada, ResultadoSalida
from expert_system.engine import inferir

router = APIRouter()

@router.post("/inferir", response_model=ResultadoSalida)
async def inferencia(contexto: ContextoEntrada):
    try:
        hechos_iniciales = contexto.dict()
        resultados = inferir(hechos_iniciales)
        return {"hechos": resultados}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
