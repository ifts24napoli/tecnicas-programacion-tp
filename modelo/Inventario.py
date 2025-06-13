class Inventario:
    def __init__(self,**datos):
        self.id_inventario = datos.get("id_inventario")
        self.stock = datos.get("stock")
        self.descripcion = datos.get("descripcion")
        self.codigo = datos.get("codigo")
        