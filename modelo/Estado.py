class Estado:
    def __init__(self,**datos):
        self.id_estado = datos.get("id_estado")
        self.descripcion = datos.get("descripcion")
        
        