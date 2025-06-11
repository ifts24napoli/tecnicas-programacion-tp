import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Autenticacion.Sesion import Sesion as Sesion
from vistas.MenuPrincipal import MenuPrincipal as MenuPrincipal
from Autenticacion.autenticacion import verificar_usuario

def main():
    sesion = Sesion()
    while True:
        if sesion.conectado:
            print("Bienvenido/a")
        else:
            print("Sesión no iniciada")
            email = str(input("E-mail: "))
            password = str(input("Contraseña: "))
            rol = verificar_usuario(email, password)
            if rol:
                sesion.conectar(email, rol)
                print("Ingreso exitoso")
                MenuPrincipal(sesion)
        
if __name__ == "__main__":
    main()