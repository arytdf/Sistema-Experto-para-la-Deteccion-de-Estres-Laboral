# expert_system/rules.py

def antecedente_ejemplo(hechos):
    # Por ejemplo, si en hechos existe "temperatura" y es mayor a 30
    return hechos.get("temperatura", 0) > 30

def conclusion_ejemplo(hechos):
    return "Hace mucho calor, activar aire acondicionado"

REGLAS = [
    {
        "antecedentes": antecedente_ejemplo,
        "conclusion_key": "recomendacion",
        "conclusion_value": conclusion_ejemplo
    },
    # Agrega tantas reglas como necesites...
]
