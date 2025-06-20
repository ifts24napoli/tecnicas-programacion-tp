class TipoPago:
    def __init__(self, **datos):                                    #Este es el constructor.
        self.descripcion =  datos.get("Descripcion")
        self.estado =  datos.get("Estado")
        