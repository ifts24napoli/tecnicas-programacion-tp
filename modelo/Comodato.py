class Comodato:
    def __init__(self,**datos):
        self.id_comodato = datos.get("Id_comodato")
        self.cantidad = datos.get("Cantidad")
        self.id_inventario = datos.get("Id_inventario")
        self.id_contrato = datos.get("Id_contrato")