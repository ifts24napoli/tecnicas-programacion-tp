import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controlador.Usuarios import agregar, actualiza, consultas
from controlador.Roles import consultas as consultasRol
from modelo.Usuarios import Usuarios
from tkinter import *
from tkinter import ttk
import ast
from tkinter import messagebox

VENTANA_TITULO = "ABM Usuarios"

class MenuUsuario:
    def __init__(self):
        self.menuGui = Tk()
        self.menuGui.title("Menú de Usuario")
        self.menuGui.geometry("300x300")

        frame = ttk.Frame(self.menuGui, padding=20)
        frame.pack(expand=True)

        opciones = [
            ("Salir", self.salir),
            ("Crear Usuario", self.usuarioNuevo),
            ("Modificar Usuario", self.listarUsuarios),
            ("Eliminar Usuario", self.eliminarUsuario)
        ]

        for texto, comando in opciones:
            boton = ttk.Button(frame, text=texto, command=comando)
            boton.pack(fill="x", pady=5)

        self.menuGui.mainloop()

    def verificoRol(self):
        return consultasRol("SELECT id_rol, tipo_rol FROM roles")

    def usuarioNuevo(self):
        usuarios = Usuarios()
        print("Alta de Usuarios del Sistema")
        usuarios.nombre = input("Ingrese Nombre del Usuario: ")
        usuarios.apellido = input("Ingrese Apellido del Usuario: ")
        usuarios.mail = input("Ingrese Mail: ")
        respuesta = dict(self.verificoRol())

        while True:
            usuarios.id_rol = int(input("Seleccione un Rol ID: "))
            if usuarios.id_rol in respuesta:
                confirmacion = input("Confirma el cambio s/n? ")
                if confirmacion.lower() == "s":
                    resultado = agregar(usuarios)
                    print(resultado[1])
                else:
                    print("No se guardaron los cambios")
                break
            print("Debe seleccionar un ID Rol de la lista")

    def listarUsuarios(self):
        resultados = consultas("""
            SELECT U.id_usuario, U.nombre, U.apellido, U.dni, U.Mail, R.tipo_rol 
            FROM usuarios AS U
            INNER JOIN roles AS R ON R.id_rol = U.id_rol
        """)

        if not resultados:
            print("No se encontraron usuarios.")
            return

        ventana = Toplevel(self.menuGui)
        ventana.title("Lista de Usuarios")
        ventana.geometry("800x300")

        columnas = ("ID", "Nombre", "Apellido", "DNI", "Mail", "Rol")
        tree = ttk.Treeview(ventana, columns=columnas, show="headings")

        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=120)

        usuarios_limpios = []

        for fila in resultados:
            # Paso 1: convertir a tupla real si viene como string
            if isinstance(fila, str):
                fila = ast.literal_eval(fila)

            # Paso 2: limpiar comillas simples (solo si se necesita)
            fila_limpia = tuple(
                str(dato).strip().strip("'") if dato is not None else "" for dato in fila
            )

            usuarios_limpios.append(fila_limpia)

        for fila in usuarios_limpios:
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
        ventana_edicion.title("Modificar Usuario")
        ventana_edicion.geometry("400x300")

        id_usuario, nombre, apellido, dni, mail, rol = valores

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

        ttk.Label(ventana_edicion, text="Mail:").pack()
        entry_mail = ttk.Entry(ventana_edicion)
        entry_mail.insert(0, mail)
        entry_mail.pack()

        ttk.Label(ventana_edicion, text="Rol:").pack()
        roles = dict(self.verificoRol())
        combo_rol = ttk.Combobox(ventana_edicion, values=list(roles.values()))
        combo_rol.set(rol)
        combo_rol.pack()

        def guardarCambios():
            usuario = Usuarios()
            usuario.nombre = entry_nombre.get()
            usuario.apellido = entry_apellido.get()
            usuario.dni = entry_dni.get()
            usuario.mail = entry_mail.get()

            for k, v in roles.items():
                if v == combo_rol.get():
                    usuario.id_rol = k
                    break

            actualiza("id_usuario", id_usuario, usuario)
            
            messagebox.showinfo("Éxito", "Usuario actualizado correctamente")
            ventana_edicion.destroy()
            ventana_listado.destroy()
            self.listarUsuarios()
            

        ttk.Button(ventana_edicion, text="Guardar Cambios", command=guardarCambios).pack(pady=10)

    def abrirFormilarioUsuarioNuevo(self):
        usuario = Usuarios()
        ventana = Toplevel(self.menuGui)
        ventana.title("Lista de Usuarios")
        ventana.geometry("800x300")
        print("Hola Mundo")
        
    def eliminarUsuario(self):
        print("Elimino Usuario")

    def salir(self):
        self.menuGui.destroy()

