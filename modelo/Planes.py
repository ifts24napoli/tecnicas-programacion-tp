class Planes:
    def __init__(self,**datos):
        self.descripcion = datos.get("Descripción")
        self.precio = datos.get("Precio")
        