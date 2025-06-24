@echo off
python -c "
import yaml, json, os;
with open('data/reglas.yml', 'r', encoding='utf-8') as yml_file:
    data = yaml.safe_load(yml_file);
with open('data/reglas.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=2);
print('Conversión YML→JSON completada');
"
pause