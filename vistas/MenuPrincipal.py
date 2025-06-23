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

STICKY_PROP = "w"
TEXTO_CERRAR_SESION = "Cerrar Sesión"
TEXTO_CLIENTES = "Gestión Clientes"
TEXTO_COMODATOS= "Gestión Comodatos"
TEXTO_CONTRATO = "Gestión Contratos"
TEXTO_FACTURAS= "Gestión Facturas"
TEXTO_INVENTARIO = "Gestión Inventarios"
TEXTO_PLANES = "Gestión Planes"
TEXTO_REPORTES= "Gestión Reportes"
TEXTO_ROLES = "Rol "
TEXTO_SESION_USUARIO = "Bienvenido/a "
TEXTO_TIPOS_PAGOS = "Gestión Tipo de Pagos"
VENTANA_TITULO = "Menú Principal"
TEXTO_USUARIOS = "Gestión Usuarios"
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
    #marco_usuario = ttk.Frame(root, bg="lightgray", bd=2, relief=ttk.SOLID)
    #marco_usuario.pack(padx=10, pady=10)
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    marco_usuario = ttk.Frame(frm)
    marco_usuario.pack(side=TOP)
    root.resizable(width=False, height=False)
    root.geometry("250x400")
    texto_sesion_usuario = ttk.Label(marco_usuario, text=TEXTO_SESION_USUARIO+sesion.nombre_usuario)
    texto_sesion_usuario.grid(column=0, row=1, sticky=STICKY_PROP)
    texto__ROLES = ttk.Label(marco_usuario, text=TEXTO_ROLES+sesion.tipo_rol)
    texto__ROLES.grid(column=0, row=2, sticky=STICKY_PROP)
    btn_usuarios = ttk.Button(frm, text=TEXTO_USUARIOS, command=MenuUsuario)
    btn_usuarios.grid(column=0, row=3, sticky=STICKY_PROP)
    btn_clientes = ttk.Button(frm, text=TEXTO_CLIENTES, command=MenuCliente)
    btn_clientes.grid(column=0, row=4, sticky=STICKY_PROP)
    btn_planes = ttk.Button(frm, text=TEXTO_PLANES, command=lambda: abmPlanes())
    btn_planes.grid(column=0, row=5, sticky=STICKY_PROP)
    btn_inventario = ttk.Button(frm, text=TEXTO_INVENTARIO, command=lambda: abmInventario())
    btn_inventario.grid(column=0, row=6, sticky=STICKY_PROP)
    btn_tipo_pagos = ttk.Button(frm, text=TEXTO_TIPOS_PAGOS, command=lambda: abmTipoPago())
    btn_tipo_pagos.grid(column=0, row=7, sticky=STICKY_PROP)
    btn_contratos = ttk.Button(frm, text=TEXTO_CONTRATO, command=lambda: abmContratos())
    btn_contratos.grid(column=0, row=8, sticky=STICKY_PROP)
    btn_comodatos = ttk.Button(frm, text=TEXTO_COMODATOS, command=lambda: abmComodato())
    btn_comodatos.grid(column=0, row=9, sticky=STICKY_PROP)
    btn_facturas = ttk.Button(frm, text=TEXTO_FACTURAS, command=lambda: abmFacturacion())
    btn_facturas.grid(column=0, row=10, sticky=STICKY_PROP)
    btn_reportes = ttk.Button(frm, text=TEXTO_REPORTES, command=lambda: reporteFinanciero())
    btn_reportes.grid(column=0, row=11, sticky=STICKY_PROP)
    
    btn_usuarios.config(state=STATE_DISABLED)
    btn_clientes.config(state=STATE_DISABLED)
    btn_planes.config(state=STATE_DISABLED)
    btn_inventario.config(state=STATE_DISABLED)
    btn_tipo_pagos.config(state=STATE_DISABLED)
    btn_contratos.config(state=STATE_DISABLED)
    btn_comodatos.config(state=STATE_DISABLED)
    btn_facturas.config(state=STATE_DISABLED)
    btn_reportes.config(state=STATE_DISABLED)
    
    match sesion.rol_usuario:
        case 1: 
                btn_usuarios.config(state=STATE_ENABLED)
                btn_clientes.config(state=STATE_ENABLED)
                btn_planes.config(state=STATE_ENABLED)
                btn_inventario.config(state=STATE_ENABLED)
                btn_tipo_pagos.config(state=STATE_ENABLED)
                btn_contratos.config(state=STATE_ENABLED)
                btn_comodatos.config(state=STATE_ENABLED)
                btn_facturas.config(state=STATE_ENABLED)
                btn_reportes.config(state=STATE_ENABLED)
        case 2:
                btn_clientes.config(state=STATE_ENABLED)
                btn_planes.config(state=STATE_ENABLED)
                btn_inventario.config(state=STATE_ENABLED)
                btn_tipo_pagos.config(state=STATE_ENABLED)
                btn_contratos.config(state=STATE_ENABLED)
                btn_comodatos.config(state=STATE_ENABLED) 
        case 3:
                btn_facturas.config(state=STATE_ENABLED)
                btn_reportes.config(state=STATE_ENABLED)             
    
    def cerrar_sesion():
        sesion.desconectar()
        root.destroy()
        main()
    btn_cerrar_sesion = ttk.Button(marco_usuario, text=TEXTO_CERRAR_SESION, command=cerrar_sesion)
    btn_cerrar_sesion.grid(column=0, row=12, sticky=STICKY_PROP)
    root.mainloop()