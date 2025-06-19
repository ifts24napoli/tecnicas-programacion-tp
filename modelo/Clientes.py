class Clientes:
    def __init__(self,**datos):
        self.nombre = datos.get("Nombre")
        self.apellido = datos.get("Apellido")
        self.dni = datos.get("DNI")
        self.cuit = datos.get("Cuit")
        self.mail = datos.get("Mail")
        self.direccion = datos.get("Direccion")
        self.cuit = datos.get("Cuit")

