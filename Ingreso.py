import sys, os
from tkinter import *
from tkinter import ttk
from dotenv import load_dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Autenticacion.Sesion import Sesion as Sesion
from Autenticacion.autenticacion import verificar_usuario

ANCHO_VENTANA = 250
ALTO_VENTANA = 100
ENV_MEDIO = "MEDIO"
TEXTO_BIENVENIDA = "Bienvenido/a"
TEXTO_EMAIL = "Email: "
TEXTO_INGRESAR = "Ingresar"
TEXTO_INGRESO_EXITOSO = "Ingreso exitoso"
TEXTO_NO_SE_PUDO_CONECTAR = "No se pudo conectar"
TEXTO_SESION_NO_INICIADA = "Sesión no iniciada"
TEXTO_PASSWORD = "Contraseña: "
VENTANA_TITULO = "TP Programación"

def main():
    sesion = Sesion()
    medio = os.getenv("MEDIO")
    if medio=="gui":
        from vistas.MenuPrincipal import GuiMenuPrincipal as GuiMenuPrincipal
        root = Tk()
        root.title(VENTANA_TITULO)
        root.resizable(width=False, height=False)
        width = 0
        height = 0
        ancho_pantalla = root.winfo_screenwidth()
        alto_pantalla = root.winfo_screenheight()
        x_central = (ancho_pantalla - width) // 2
        y_central = (alto_pantalla - height) // 2
        root.geometry(f"{width}x{height}+{x}+{y}")
        root.geometry("250x120")
        frm = ttk.Frame(root, padding=10)
        frm.grid()
        ttk.Label(frm, text=TEXTO_SESION_NO_INICIADA).grid(column=0, row=0)
        ttk.Label(frm, text=TEXTO_EMAIL).grid(column=0, row=1, sticky="w")
        ttk.Label(frm, text=TEXTO_PASSWORD).grid(column=0, row=2, sticky="w")
        entrada_usuario = ttk.Entry(frm)
        entrada_usuario.grid(column=1, row=1, sticky="w")
        entrada_password = ttk.Entry(frm, show="*")
        entrada_password.grid(column=1, row=2, sticky="w")
        estado_sesion = ttk.Label(frm, foreground="red")
        estado_sesion.grid(column=0, row=4, sticky="w")
        def ingresar():
            email = entrada_usuario.get()
            password = entrada_password.get()
            rol_id, tipo_rol = verificar_usuario(email, password)
            if rol_id:
                sesion.conectar(email, rol_id, tipo_rol)
                root.destroy()
                GuiMenuPrincipal(sesion)
            else:
                estado_sesion.config(text=TEXTO_NO_SE_PUDO_CONECTAR)
        btn_ingresar = ttk.Button(frm, text=TEXTO_INGRESAR, command=ingresar)
        btn_ingresar.grid(column=0, row=3, sticky="w")
        ttk.Label().grid(column=0, row=2, sticky="w")
        root.mainloop()
        
    else:
        from vistas.MenuPrincipal import MenuPrincipal as MenuPrincipal
        while True:
            if sesion.conectado:
                print(TEXTO_BIENVENIDA)
            else:
                print(TEXTO_SESION_NO_INICIADA)
                email = str(input(TEXTO_EMAIL))
                password = str(input(TEXTO_PASSWORD))
                rol_id, tipo_rol = verificar_usuario(email, password)
                if rol_id:
                    sesion.conectar(email, rol_id, tipo_rol)
                    print()
                    MenuPrincipal(sesion)

if __name__ == "__main__":
    main()
