class Clientes:
    def __init__(self,**datos):
        self.nombre = datos.get("Nombre")
        self.apellido = datos.get("Apellido")
        self.mail = datos.get("Mail")
        self.cuit = datos.get("Cuit")