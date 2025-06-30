import json

class CargaBase:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.datos = self.cargar_datos()
    
    def cargar_datos(self):
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
            return datos
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.ruta_archivo}")
            return {"sintomas": {}, "reglas": [], "diagnosticos": {}}
        except json.JSONDecodeError:
            print(f"Error: El archivo {self.ruta_archivo} no tiene formato JSON válido")
            return {"sintomas": {}, "reglas": [], "diagnosticos": {}}