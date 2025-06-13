class Contratos:
    def __init__(self,**datos):
        self.id_contrato = datos.get("id_contrato")
        self.fecha_alta = datos.get("fecha_alta")
        self.fecha_baja = datos.get("fecha_baja")
        self.motivo_baja = datos.get("motivo_baja")
        self.id_cliente = datos.get("id_cliente")
        self.id_plan = datos.get("id_plan")
        self.id_tipo_pago = datos.get("id_tipo_pago")
        self.id_estado = datos.get("id_estado")