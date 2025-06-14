import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tkinter import *
from tkinter import ttk
import ast
from tkinter import messagebox
from controlador.Roles import consultas as consularRol

class PruebaMenu:
    def __init__(self, nombreMenu):
        self.menuGui = Tk()
        self.nombreMenu = nombreMenu
        self.opciones = None
        self.objeto = None
        self.comoBox = []
        self.select = None
        self.camposIgnorados = []
        self.preparoOpciones()

    def crearMenu(self):
        self.menuGui.title(self.nombreMenu)
        self.menuGui.geometry("300x300")

        frame = ttk.Frame(self.menuGui, padding=20)
        frame.pack(expand=True)
        for opcione, comando in self.opciones:
            boton = ttk.Button(frame, text=opcione, command=comando)
            boton.pack(fill="x", pady=5)
            
        frame = ttk.Frame(self.menuGui, padding=20)
        frame.pack(expand=True)
        self.menuGui.mainloop()
    
    def salir(self):
        self.menuGui.destroy()    
        
    def abrirFormularioUsuarioNuevo(self):
        ventana = Toplevel(self.menuGui)
        ventana.title(f"Crear {self.nombreMenu}")
        ventana.geometry("800x300")
        for atributo in self.objeto.__dict__:
            if atributo not in self.camposIgnorados:
                ttk.Label(ventana, text=f"{atributo.capitalize()}:").pack()
                entrada = ttk.Entry(ventana)
                entrada.pack()
        
        for atributo, select in self.comoBox:
            ttk.Label(ventana, text=f"{atributo}:").pack()
            datos = dict(self.obtengoDatosComboBox(select))
            entrada = ttk.Combobox(ventana, values=list(datos.values()))
            entrada.set(list(datos.values())[0])
            entrada.pack()
            setattr(self, f"entry_{atributo}", entrada)  # Crea self.entry_nombre, etc.
            
    def listarUsuarios(self):
        print("Modifico")
        
    def eliminarUsuario(self):
        print("Elimino")            
        
    def preparoOpciones(self):
        print(self.nombreMenu)
        self.opciones = [
            ("Salir", self.salir),
            (f"Crear {self.nombreMenu}", self.abrirFormularioUsuarioNuevo),
            (f"Modificar {self.nombreMenu}", self.listarUsuarios),
            (f"Eliminar {self.nombreMenu}", self.eliminarUsuario)
            ]
        
    def obtengoDatosComboBox(self, select):  
        return consularRol(select) 