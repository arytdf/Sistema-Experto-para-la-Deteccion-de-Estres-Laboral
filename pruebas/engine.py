# tests/test_engine.py

import pytest
from expert_system.engine import inferir

def test_inferir_regla_simple():
    datos = {"temperatura": 35}
    salida = inferir(datos)
    assert "recomendacion" in salida
    assert salida["recomendacion"] == "Hace mucho calor, activar aire acondicionado"
