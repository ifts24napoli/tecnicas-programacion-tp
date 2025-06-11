class Sesion:
    def __init__(self):
        self.conectado = False
        self.email_usuario = ""
        self.rol_usuario = 0

    def conectar(self, email, rol):
        self.conectado = True
        self.email_usuario = email
        self.rol_usuario = rol

    def desconectar(self):
        self.conectado = False