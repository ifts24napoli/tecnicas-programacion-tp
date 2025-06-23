import sys, os
from tkinter import *
from tkinter import ttk
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from vistas.ABMUsuario import MenuUsuario
from vistas.ABMClientes import MenuCliente
from Autenticacion.Sesion import Sesion
from vistas.ABMComodato import abmComodato
from vistas.ABMContratos import abmContratos
from vistas.ABMFacturacion import abmFacturacion
from vistas.ABMInventario import abmInventario
from vistas.ABMPlanes import abmPlanes
from vistas.ABMTipoPago import abmTipoPago
from vistas.ReporteFinanciero import menu as reporteFinanciero

ALTO_FILA = 35
ALTO_MARCO_USUARIO = 90
ANCHO_VENTANA = 230
STICKY_PROP = "w"
TEXTO_CERRAR_SESION = "Cerrar Sesión"
TEXTO_CLIENTES = "Clientes"
TEXTO_COMODATOS= "Comodatos"
TEXTO_CONTRATO = "Contratos"
TEXTO_FACTURAS= "Facturas"
TEXTO_GESTION = "Gestión "
TEXTO_INVENTARIO = "Inventarios"
TEXTO_PLANES = "Planes"
TEXTO_REPORTES= "Reportes"
TEXTO_ROLES = "• "
TEXTO_SESION_USUARIO = "Bienvenido/a "
TEXTO_TIPOS_PAGOS = "Tipo de Pagos"
VENTANA_TITULO = "Menú Principal"
TEXTO_USUARIOS = "Usuarios"
STATE_DISABLED = "disabled"
STATE_ENABLED = "enabled"

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
    root.resizable(0, 0)
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    marco_usuario = ttk.Frame(frm)
    marco_usuario.pack(side="top")
    texto_sesion_usuario = ttk.Label(marco_usuario, text=TEXTO_SESION_USUARIO+sesion.nombre_usuario)
    texto_sesion_usuario.grid(column=0, row=1, sticky=STICKY_PROP)
    texto__ROLES = ttk.Label(marco_usuario, text=TEXTO_ROLES+sesion.tipo_rol)
    texto__ROLES.grid(column=0, row=2, sticky=STICKY_PROP)
    def cerrar_sesion():
        sesion.desconectar()
        root.destroy()
        main()
    btn_cerrar_sesion = ttk.Button(marco_usuario, text=TEXTO_CERRAR_SESION, command=cerrar_sesion)
    btn_cerrar_sesion.grid(column=0, row=3, sticky=STICKY_PROP)

    marco_gestion = ttk.Frame(frm)
    marco_gestion.pack(side="top")
    total_filas = 0
    match sesion.rol_usuario:
        case 1:
            total_filas = 9
            btn_usuarios = ttk.Button(marco_gestion, text=TEXTO_GESTION+TEXTO_USUARIOS, command=MenuUsuario)
            btn_usuarios.grid(column=0, row=1, sticky=STICKY_PROP)
            btn_clientes = ttk.Button(marco_gestion, text=TEXTO_GESTION+TEXTO_CLIENTES, command=MenuCliente)
            btn_clientes.grid(column=0, row=2, sticky=STICKY_PROP)
            btn_planes = ttk.Button(marco_gestion, text=TEXTO_GESTION+TEXTO_PLANES, command=lambda: abmPlanes())
            btn_planes.grid(column=0, row=3, sticky=STICKY_PROP)
            btn_inventario = ttk.Button(marco_gestion, text=TEXTO_GESTION+TEXTO_INVENTARIO, command=lambda: abmInventario())
            btn_inventario.grid(column=0, row=4, sticky=STICKY_PROP)
            btn_tipo_pagos = ttk.Button(marco_gestion, text=TEXTO_GESTION+TEXTO_TIPOS_PAGOS, command=lambda: abmTipoPago())
            btn_tipo_pagos.grid(column=0, row=5, sticky=STICKY_PROP)
            btn_contratos = ttk.Button(marco_gestion, text=TEXTO_GESTION+TEXTO_CONTRATO, command=lambda: abmContratos())
            btn_contratos.grid(column=0, row=6, sticky=STICKY_PROP)
            btn_comodatos = ttk.Button(marco_gestion, text=TEXTO_GESTION+TEXTO_COMODATOS, command=lambda: abmComodato())
            btn_comodatos.grid(column=0, row=7, sticky=STICKY_PROP)
            btn_facturas = ttk.Button(marco_gestion, text=TEXTO_GESTION+TEXTO_FACTURAS, command=lambda: abmFacturacion())
            btn_facturas.grid(column=0, row=8, sticky=STICKY_PROP)
            btn_reportes = ttk.Button(marco_gestion, text=TEXTO_GESTION+TEXTO_REPORTES, command=lambda: reporteFinanciero())
            btn_reportes.grid(column=0, row=9, sticky=STICKY_PROP)
        case 2:
            total_filas = 6
            btn_clientes = ttk.Button(marco_gestion, text=TEXTO_GESTION+TEXTO_CLIENTES, command=MenuCliente)
            btn_clientes.grid(column=0, row=1, sticky=STICKY_PROP)
            btn_planes = ttk.Button(marco_gestion, text=TEXTO_GESTION+TEXTO_PLANES, command=lambda: abmPlanes())
            btn_planes.grid(column=0, row=2, sticky=STICKY_PROP)
            btn_inventario = ttk.Button(marco_gestion, text=TEXTO_GESTION+TEXTO_INVENTARIO, command=lambda: abmInventario())
            btn_inventario.grid(column=0, row=3, sticky=STICKY_PROP)
            btn_tipo_pagos = ttk.Button(marco_gestion, text=TEXTO_GESTION+TEXTO_TIPOS_PAGOS, command=lambda: abmTipoPago())
            btn_tipo_pagos.grid(column=0, row=4, sticky=STICKY_PROP)
            btn_contratos = ttk.Button(marco_gestion, text=TEXTO_GESTION+TEXTO_CONTRATO, command=lambda: abmContratos())
            btn_contratos.grid(column=0, row=5, sticky=STICKY_PROP)
            btn_comodatos = ttk.Button(marco_gestion, text=TEXTO_GESTION+TEXTO_COMODATOS, command=lambda: abmComodato())
            btn_comodatos.grid(column=0, row=6, sticky=STICKY_PROP)
        case 3:
            total_filas = 2
            btn_facturas = ttk.Button(marco_gestion, text=TEXTO_GESTION+TEXTO_FACTURAS, command=lambda: abmFacturacion())
            btn_facturas.grid(column=0, row=1, sticky=STICKY_PROP)
            btn_reportes = ttk.Button(marco_gestion, text=TEXTO_GESTION+TEXTO_REPORTES, command=lambda: reporteFinanciero())
            btn_reportes.grid(column=0, row=2, sticky=STICKY_PROP)
    ancho = ANCHO_VENTANA
    alto = ALTO_MARCO_USUARIO + ALTO_FILA * total_filas
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    x_central = (ancho_pantalla - ancho) // 2
    y_central = (alto_pantalla - alto) // 2
    root.geometry(f"{ancho}x{alto}+{x_central}+{y_central}")
    root.mainloop()