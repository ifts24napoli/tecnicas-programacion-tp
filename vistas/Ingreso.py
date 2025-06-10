import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from vistas.MenuPrincipal import MenuPrincipal
import Ingreso.Sesion as Sesion

def verificarUsuario(usuario, password):
    return True

def main():
    sesion = Sesion()
    while True:
        usuario = str(input("Ingrese Nombre de Usuario: "))
        password = str(input("Ingrese Contraseña: "))
        respuesta = verificarUsuario(usuario, password)
        if (respuesta):
            sesion.usuario = usuario
            sesion.conectado = True
            MenuPrincipal(sesion)
        
if __name__ == "__main__":
    main()