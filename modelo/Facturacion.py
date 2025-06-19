class Facturacion:
    def __init__(self,**datos):
        self.fecha_factura = datos.get("Fecha_Factura")
        self.monto = datos.get("Monto")
        self.estado = datos.get("Estado")
        self.id_contrato = datos.get("Id_Contrato")