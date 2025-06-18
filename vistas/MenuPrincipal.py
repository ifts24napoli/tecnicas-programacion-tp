import sys, os
from tkinter import *
from tkinter import ttk
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from vistas.ABMUsuario import MenuUsuario
from vistas.ABMClientes import MenuCliente
from Autenticacion.Sesion import Sesion

TEXTO_CERRAR_SESION = "Cerrar Sesión"
TEXTO_SESION_USUARIO = "Bienvenido/a "
TEXTO_CLIENTES = "Gestión Clientes"
TEXTO_USUARIOS = "Gestión Usuarios"
VENTANA_TITULO = "Menú Principal"

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
                MenuUsuario()
            elif opcion	 == 2:
                MenuCliente()
            elif opcion == 3:
                print("ventas")
        except ValueError:
            print("Debe ingresar un valor numérico")

def GuiMenuPrincipal(sesion:Sesion):
    from Ingreso import main
    root = Tk()
    root.title(VENTANA_TITULO)
    root.resizable(width=False, height=False)
    root.geometry("250x400")
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    texto_sesion_usuario = ttk.Label(frm, text=TEXTO_SESION_USUARIO+sesion.email_usuario)
    texto_sesion_usuario.grid(column=0, row=1, sticky="w")
    btn_usuarios = ttk.Button(frm, text=TEXTO_USUARIOS, command=MenuUsuario)
    btn_usuarios.grid(column=0, row=2, sticky="w")
    btn_clientes = ttk.Button(frm, text=TEXTO_CLIENTES, command=MenuCliente)
    btn_clientes.grid(column=0, row=3, sticky="w")
    def cerrar_sesion():
        sesion.desconectar()
        root.destroy()
        main()
    btn_cerrar_sesion = ttk.Button(frm, text=TEXTO_CERRAR_SESION, command=cerrar_sesion)
    btn_cerrar_sesion.grid(column=0, row=4, sticky="w")
    root.mainloop()