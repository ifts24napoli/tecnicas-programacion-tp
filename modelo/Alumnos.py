class Alumnos:
    def __init__(self, **datos):
        self.nombre =  datos.get("Nombre")
        self.apellido =  datos.get("Apellido")
        self.edad =  datos.get("Edad")
        self.grado = datos.get("Grado")
        self.profesor = datos.get("Profesor")