class Comodato:
    def __init__(self,**datos):
        #self.id_comodato = datos.get("Id_comodato")
        self.cantidad = datos.get("cantidad")
        self.id_inventario = datos.get("id_inventario")
        self.id_contrato = datos.get("id_contrato")