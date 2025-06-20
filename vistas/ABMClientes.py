import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controlador.Clientes import agregar, actualiza, consultas
from modelo.Clientes import Clientes
from tkinter import *
from tkinter import ttk
import ast
from tkinter import messagebox

VENTANA_TITULO = "ABM Clientes"

class MenuCliente:
    def __init__(self):
        self.menuGui = Tk()
        self.menuGui.title("Menú de Cliente")
        self.menuGui.geometry("300x300")

        frame = ttk.Frame(self.menuGui, padding=20)
        frame.pack(expand=True)

        opciones = [
            ("Salir", self.salir),
            ("Crear Cliente", self.clienteNuevo),
            ("Modificar Cliente", self.listarClientes)
        ]

        for texto, comando in opciones:
            boton = ttk.Button(frame, text=texto, command=comando)
            boton.pack(fill="x", pady=5)

        self.menuGui.mainloop()

    def clienteNuevo(self):
        clientes = Clientes()
        print("Alta de Clientes del Sistema")
        clientes.nombre = input("Ingrese Nombre del Usuario: ")
        clientes.apellido = input("Ingrese Apellido del Usuario: ")
        clientes.mail = input("Ingrese Mail: ")
        respuesta = agregar(clientes)
        print(respuesta[1])

    def listarClientes(self):
        resultados = consultas("Select * from clientes")

        if not resultados:
            print("No se encontraron usuarios.")
            return

        ventana = Toplevel(self.menuGui)
        ventana.title("Lista de Usuarios")
        ventana.geometry("800x300")

        columnas = ("ID", "Nombre", "Apellido", "DNI", "Cuit", "Mail", "Direccion")
        tree = ttk.Treeview(ventana, columns=columnas, show="headings")

        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=120)

        clientes_limpios = []

        for fila in resultados:
            if isinstance(fila, str):
                fila = ast.literal_eval(fila)

            fila_limpia = tuple(
                str(dato).strip().strip("'") if dato is not None else "" for dato in fila
            )

            clientes_limpios.append(fila_limpia)

        for fila in clientes_limpios:
            tree.insert("", "end", values=fila)
    
        tree.pack(expand=True, fill="both")

        def doble_click(event):
            item = tree.selection()
            if item:
                valores = tree.item(item[0], 'values')
                self.abrirFormularioEdicion(valores, tree , ventana)

        tree.bind("<Double-1>", doble_click)

    def abrirFormularioEdicion(self, valores, tree, ventana_listado):
        ventana_edicion = Toplevel(self.menuGui)
        ventana_edicion.title("Modificar Cliente")
        ventana_edicion.geometry("400x300")

        id_cliente, nombre, apellido, dni, cuit, mail, direccion = valores

        ttk.Label(ventana_edicion, text="Nombre:").pack()
        entry_nombre = ttk.Entry(ventana_edicion)
        entry_nombre.insert(0, nombre)
        entry_nombre.pack()

        ttk.Label(ventana_edicion, text="Apellido:").pack()
        entry_apellido = ttk.Entry(ventana_edicion)
        entry_apellido.insert(0, apellido)
        entry_apellido.pack()

        ttk.Label(ventana_edicion, text="DNI:").pack()
        entry_dni = ttk.Entry(ventana_edicion)
        entry_dni.insert(0, dni)
        entry_dni.pack()

        ttk.Label(ventana_edicion, text="Cuit:").pack()
        entry_cuit = ttk.Entry(ventana_edicion)
        entry_cuit.insert(0, cuit)
        entry_cuit.pack()

        ttk.Label(ventana_edicion, text="Mail:").pack()
        entry_mail = ttk.Entry(ventana_edicion)
        entry_mail.insert(0, mail)
        entry_mail.pack()

        ttk.Label(ventana_edicion, text="Direccion:").pack()
        entry_direccion = ttk.Entry(ventana_edicion)
        entry_direccion.insert(0, direccion)
        entry_direccion.pack()

        def guardarCambios():
            cliente = Clientes()
            cliente.nombre = entry_nombre.get()
            cliente.apellido = entry_apellido.get()
            cliente.dni = entry_dni.get()
            cliente.cuit = entry_cuit.get()
            cliente.mail = entry_mail.get()
            cliente.direccion = entry_direccion.get()

            actualiza("id_cliente", id_cliente, cliente)
            
            messagebox.showinfo("Éxito", "Cliente actualizado correctamente")
            ventana_edicion.destroy()
            ventana_listado.destroy()
            self.listarClientes()
            

        ttk.Button(ventana_edicion, text="Guardar Cambios", command=guardarCambios).pack(pady=10)

    def abrirFormularioClienteNuevo(self):
        cliente = Clientes()
        ventana = Toplevel(self.menuGui)
        ventana.title("Lista de Clientes")
        ventana.geometry("800x300")
        print("Esta es una prueba del puto cache de mierda")
        
    def eliminarUsuario(self):
        print("Elimino Cliente")

    def salir(self):
        self.menuGui.destroy()