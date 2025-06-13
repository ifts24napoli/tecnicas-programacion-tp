class Comodato:
    def __init__(self,**datos):
        self.cantidad = datos.get("Cantidad")
        self.id_inventario = datos.get("Id_inventario")
        self.id_contrato = datos.get("Id_contrato")