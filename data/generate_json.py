# data/generate_json.py
import yaml, json
from pathlib import Path

BASE = Path(__file__).parent
YAML_PATH = BASE / "reglas.yml"
JSON_PATH = BASE / "reglas.json"

def normalize_keys(respuestas: dict) -> dict:
    new = {}
    for k, v in respuestas.items():
        key = None
        ks = str(k).lower()
        if ks in ("false", "no"):
            key = "NO"
        elif ks in ("true", "si", "sí"):
            key = "SI"
        else:
            key = str(k)
        new[key] = v
    return new

# Carga YAML en UTF-8
with open(YAML_PATH, encoding="utf-8") as yf:
    reglas_yaml = yaml.safe_load(yf)

# Normaliza cada nodo
reglas_norm = {}
for nodo, contenido in reglas_yaml.items():
    if "RESPUESTAS" in contenido:
        contenido["RESPUESTAS"] = normalize_keys(contenido["RESPUESTAS"])
    reglas_norm[nodo] = contenido

# Escribe JSON en UTF-8 con claves SI/NO
with open(JSON_PATH, "w", encoding="utf-8") as jf:
    json.dump(reglas_norm, jf, ensure_ascii=False, indent=2)

print("reglas.json regenerado con claves SI/NO correctamente normalizadas.")


