import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from vistas.ABMUsuario import abmUsuarios
from vistas.ABMClientes import abmClientes

def despejar():
    os.system("cls" if os.name == "nt" else "clear")

def MenuPrincipal(sesion):
    while True:
        print(f""" ## {sesion.email_usuario} ##
            Selecciones una de las siguientes opciones:
            \t0 Para Salir
            \t1 Gestion de Ususario
            \t2 Gestion de Clientes 
            """)
        opcion = int(input("Ingrese Alguna Opcion: "))
        if opcion == 0:
            break
        elif opcion == 1:
            abmUsuarios()
        elif opcion	 == 2:
            abmClientes()