import sys, os
from tkinter import *
from tkinter import ttk
from dotenv import load_dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Autenticacion.Sesion import Sesion as Sesion
from vistas.MenuPrincipal import MenuPrincipal as MenuPrincipal
from Autenticacion.autenticacion import verificar_usuario

TEXTO_SESION_NO_INICIADA = "Sesión no iniciada"
TEXTO_EMAIL = "Email: "
TEXTO_PASSWORD = "Contraseña: "
TEXTO_INGRESAR = "Ingresar"

def main():
    sesion = Sesion()
    medio = os.getenv('MEDIO')
    if medio=="gui":
        root = Tk()
        frm = ttk.Frame(root, padding=10)
        frm.grid()
        ttk.Label(frm, text=TEXTO_SESION_NO_INICIADA).grid(column=0, row=0)
        ttk.Label(frm, text=TEXTO_EMAIL).grid(column=0, row=1, sticky="w")
        ttk.Label(frm, text=TEXTO_PASSWORD).grid(column=0, row=2, sticky="w")
        entrada_usuario = ttk.Entry(frm).grid(column=1, row=1, sticky="w")
        entrada_password = ttk.Entry(frm).grid(column=1, row=2, sticky="w")
        btn_ingresar = ttk.Button(frm, text=TEXTO_INGRESAR)
        btn_ingresar.grid(column=0, row=3, sticky="w")
        ttk.Label().grid(column=0, row=2, sticky="w")
        root.mainloop()
    else:
        while True:
            if sesion.conectado:
                print("Bienvenido/a")
            else:
                print(TEXTO_SESION_NO_INICIADA)
                email = str(input(TEXTO_EMAIL))
                password = str(input(TEXTO_PASSWORD))
                rol = verificar_usuario(email, password)
                if rol:
                    sesion.conectar(email, rol)
                    print("Ingreso exitoso")
                    MenuPrincipal(sesion)

if __name__ == "__main__":
    main()