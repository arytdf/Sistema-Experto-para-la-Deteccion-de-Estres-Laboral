class MotorInferencia:
    def __init__(self, conocimiento):
        self.sintomas = conocimiento.get('sintomas', {})
        self.reglas = conocimiento.get('reglas', [])
        self.diagnosticos = conocimiento.get('diagnosticos', {})
        
        self.hechos_conocidos = set()
        self.diagnostico_actual = None

    def agregar_hecho(self, hecho):
        self.hechos_conocidos.add(hecho)
        self.evaluar_reglas()

    def evaluar_reglas(self):
        for regla in self.reglas:
            condiciones = regla.get('condiciones', [])
            diagnostico = regla.get('diagnostico', 'CA')
            
            # Verificar si todas las condiciones se cumplen
            if all(cond in self.hechos_conocidos for cond in condiciones):
                self.diagnostico_actual = diagnostico
                return True
        
        return False

    def obtener_proximo_sintoma(self):
        # Primero verificar si ya tenemos un diagnóstico
        if self.diagnostico_actual is not None:
            return None
    
        # Buscar el próximo síntoma no preguntado
        for id_sintoma in self.sintomas:
            sintoma = self.sintomas[id_sintoma]
        
            # Verificar si el síntoma no ha sido preguntado
            if (id_sintoma not in self.hechos_conocidos and 
                f"!{id_sintoma}" not in self.hechos_conocidos and
                not any(f"{id_sintoma}:" in h for h in self.hechos_conocidos)):
                return sintoma
    
        return None
    
    def obtener_sintoma_por_id(self, id_sintoma):
        return self.sintomas.get(id_sintoma, None)