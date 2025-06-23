class Sesion:
    def __init__(self):
        self.conectado = False
        self.email_usuario = ""
        self.rol_usuario = 0
        self.tipo_rol = None

    def conectar(self, email, nombre, rol, tipo_rol):
        self.conectado = True
        self.email_usuario = email
        self.nombre_usuario = nombre
        self.rol_usuario = rol
        self.tipo_rol = tipo_rol

    def reset(self):
        self.conectado = False
        self.email_usuario = ""
        self.nombre_usuario = ""
        self.rol_usuario = 0
        self.tipo_rol = None

    def desconectar(self):
        self.reset()