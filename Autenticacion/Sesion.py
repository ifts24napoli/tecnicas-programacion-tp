class Sesion:
    def __init__(self):
        self.conectado = False
        self.email_usuario = ""
        self.rol_usuario = 0
        self.tipo_rol = None

    def conectar(self, email, rol, tipo_rol):
        self.conectado = True
        self.email_usuario = email
        self.rol_usuario = rol
        self.tipo_rol = tipo_rol

    def desconectar(self):
        self.conectado = False