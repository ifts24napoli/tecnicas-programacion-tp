class Clientes:
    def __init__(self,**datos):
        self.nombre = datos.get("Nombre")
        self.apellido = datos.get("Apellido")
        self.dni = datos.get("DNI")
        self.cuit = datos.get("Cuit")
        self.mail = datos.get("Mail")
<<<<<<< HEAD
        self.direccion = datos.get("Direccion")
=======
        self.cuit = datos.get("Cuit")
>>>>>>> 4f4bf7c99375aba09467fbc696ea582d4bdadd29
