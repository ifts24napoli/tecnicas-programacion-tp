class Tipo_pago:
    def __init__(self,**datos):
        self.id_tipo_pago = datos.get("id_tipo_pago")
        self.descripcion = datos.get("descripcion")
        
        