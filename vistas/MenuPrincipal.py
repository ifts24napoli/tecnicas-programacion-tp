import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from vistas.ABMUsuario import abmUsuarios
from vistas.ABMClientes import abmClientes
from Autenticacion.Sesion import Sesion

def despejar():
    os.system("cls" if os.name == "nt" else "clear")
    
    
def creoMenu(sesion:Sesion):
    menu = ['Hola: ' + sesion.email_usuario]
    menu.append('\tSelecciones una de las siguientes opciones:')
    if sesion.rol_usuario == 1:
        menu.append('\t0 Para Salir')
        menu.append('\t1 Gestion de Ususario')
        menu.append('\t2 Gestion de Clientes ')
        menu.append('\t3 Gestion de Ventas')
    elif sesion.rol_usuario == 2:
        menu.append('\t0 Para Salir')
        menu.append('\t2 Gestion de Clientes')
    elif sesion.rol_usuario == 3:
         menu.append('\t0 Para Salir')
         menu.append('\t3 Ventas')  
    for valor in menu:
        print(valor)


def MenuPrincipal(sesion:Sesion):
    while True:
        despejar()
        creoMenu(sesion)
        try:
            opcion = int(input("Ingrese Alguna Opcion: "))
            if opcion == 0:
                sesion.desconectar()
                break
            elif opcion == 1:
                despejar()
                abmUsuarios()
            elif opcion	 == 2:
                abmClientes()
            elif opcion == 3:
                print("ventas")    
        except ValueError:
            print("Debe ingresar un valor numérico")

