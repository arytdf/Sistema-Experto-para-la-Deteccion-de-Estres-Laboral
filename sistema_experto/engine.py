# expert_system/engine.py

from expert_system.rules import REGLAS

def inferir(datos_contexto: dict) -> dict:
    """
    Ejecuta el motor de inferencia sobre un conjunto de hechos iniciales
    (datos_contexto). Recorre cada regla y, si se cumple la condición,
    añade la conclusión al conjunto de hechos. Devuelve un diccionario
    con los resultados inferidos.
    """
    hechos = datos_contexto.copy()
    cambios = True

    while cambios:
        cambios = False
        for regla in REGLAS:
            if regla["antecedentes"](hechos) and regla["conclusion_key"] not in hechos:
                hechos[regla["conclusion_key"]] = regla["conclusion_value"](hechos)
                cambios = True

    return hechos
