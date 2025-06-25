import yaml
import json
from pathlib import Path

BASE = Path(__file__).parent  # esto ya apunta a .../Prueba/data
YAML_PATH = BASE / "reglas.yml"
JSON_PATH = BASE / "reglas.json"

def normalize_keys(respuestas: dict) -> dict:
    new = {}
    for k, v in respuestas.items():
        ks = str(k).strip().lower()
        if ks in ("false", "no"):
            key = "NO"
        elif ks in ("true", "si", "sí"):
            key = "SI"
        else:
            key = str(k)
        new[key] = v
    return new

# Carga YAML unificado
with open(YAML_PATH, encoding="utf-8") as yf:
    struct = yaml.safe_load(yf)

# Reconstruye el JSON con la estructura de gimnasia.json
json_struct = {
    "__v": struct.get("__v", 1),
    "description": struct.get("description", ""),
    "entries": [],
    "final_message": struct.get("final_message", "")
}

for entry in struct.get("entries", []):
    item = {
        "name": entry.get("name"),
        "description": entry.get("description", ""),
        "props": {}
    }
    for prop_key, prop_val in entry.get("props", {}).items():
        if prop_key == "RESPUESTAS" and isinstance(prop_val, dict):
            item["props"][prop_key] = normalize_keys(prop_val)
        else:
            item["props"][prop_key] = prop_val
    json_struct["entries"].append(item)

# Escribe JSON en data/reglas.json
with open(JSON_PATH, "w", encoding="utf-8") as jf:
    json.dump(json_struct, jf, ensure_ascii=False, indent=2)

print("[generate_json] reglas.json regenerado con la estructura unificada correctamente.")


