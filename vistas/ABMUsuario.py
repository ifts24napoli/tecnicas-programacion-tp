from tkinter import *
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tkinter import messagebox
from controlador.Usuarios import agregar, actualiza, consultas, elimina
from controlador.Roles import consultas as consultasRol
from modelo.Usuarios import Usuarios
from tkinter import ttk
import ast
from vistas.PruebaMenu import PruebaMenu
from modelo.Clientes import Clientes

class MenuUsuario:
    def __init__(self):
        self.menuGui = Tk()
        self.menuGui.title("Menú de Usuario")
        self.menuGui.geometry("300x300")

        frame = ttk.Frame(self.menuGui, padding=20)
        frame.pack(expand=True)

        opciones = [
            ("Salir", self.salir),
            ("Crear Usuario", self.abrirFormularioUsuarioNuevo),
            ("Modificar Usuario", lambda: self.listarUsuarios("mod")),
            ("Eliminar Usuario", lambda: self.listarUsuarios("del"))
        ]

        for texto, comando in opciones:
            boton = ttk.Button(frame, text=texto, command=comando)
            boton.pack(fill="x", pady=5)

        self.menuGui.mainloop()

    def verificoRol(self):
        return consultasRol("SELECT id_rol, tipo_rol FROM roles")
    
    def veridicoMail(self,mail):
        return consultas (f"""select count(*) 
                            from usuarios 
                            where mail = '{mail}' """)

    def listarUsuarios(self,tipo):
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
                self.abrirFormularioEdicion(valores, tree , ventana, tipo)

        tree.bind("<Double-1>", doble_click)

    def abrirFormularioEdicion(self, valores, tree, ventana_listado, tipo):
        ventana_edicion = Toplevel(self.menuGui)
        if tipo == "mod":
            ventana_edicion.title("Modificar Usuario")
        else: ventana_edicion.title("Eliminar Usuario")    
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
        
        ttk.Label(ventana_edicion, text="Password:").pack()
        entry_password = ttk.Entry(ventana_edicion, show="*")
        entry_password.pack()

        ttk.Label(ventana_edicion, text="Rol:").pack()
        roles = dict(self.verificoRol())
        combo_rol = ttk.Combobox(ventana_edicion, values=list(roles.values()))
        combo_rol.set(rol)
        combo_rol.pack()
        
        if tipo != "mod":
            entry_nombre.config(state='readonly') 
            entry_apellido.config(state='readonly')
            entry_dni.config(state='readonly')
            entry_mail.config(state='readonly')
            entry_password.config(state='readonly')
            combo_rol.config(state='disabled')
            
        def guardarCambios():
            usuario = Usuarios()
            usuario.nombre = entry_nombre.get()
            usuario.apellido = entry_apellido.get()
            usuario.dni = entry_dni.get()
            usuario.mail = entry_mail.get()
            if entry_password.get() != "":
                usuario.pwd = entry_password.get()

            for k, v in roles.items():
                if v == combo_rol.get():
                    usuario.id_rol = k
                    break
                         
            actualiza("id_usuario", id_usuario, usuario)
            
            messagebox.showinfo("Éxito", "Usuario actualizado correctamente")
            ventana_edicion.destroy()
            ventana_listado.destroy()
            self.listarUsuarios("mod")
            
        def eliminarUsuario():
            elimina('id_usuario', id_usuario)
            messagebox.showinfo('Mensaje', "Usuario Eliminado") 
            ventana_edicion.destroy()
            ventana_listado.destroy()
            self.listarUsuarios("del")
              
        if tipo == "mod":
            ttk.Button(ventana_edicion, text="Guardar Cambios", command=guardarCambios).pack(pady=10)
        else: ttk.Button(ventana_edicion, text="Eliminar", command=eliminarUsuario).pack(pady=10)    

    def abrirFormularioUsuarioNuevo(self):
        ventana = Toplevel(self.menuGui)
        ventana.title("Crear Usuario")
        ventana.geometry("500x350")
        ttk.Label(ventana, text="Nombre:").pack()
        entry_nombre = ttk.Entry(ventana)
        entry_nombre.pack()
        ttk.Label(ventana, text="Apellido:").pack()
        entry_apellido = ttk.Entry(ventana)
        entry_apellido.pack()
        ttk.Label(ventana, text="Dni:").pack()
        entry_dni = ttk.Entry(ventana)
        entry_dni.pack()
        ttk.Label(ventana, text="Mail:").pack()
        entry_mail = ttk.Entry(ventana)
        entry_mail.pack()
        ttk.Label(ventana, text="Contraseña:").pack()
        entry_password = ttk.Entry(ventana, show="*")
        entry_password.pack()
        ttk.Label(ventana, text="Repetir Contraseña:").pack()
        entry_password_repetido = ttk.Entry(ventana, show="*")
        entry_password_repetido.pack()
        
        ttk.Label(ventana, text="Rol:").pack()
        roles = dict(self.verificoRol())
        combo_rol = ttk.Combobox(ventana, values=list(roles.values()))
        combo_rol.set(list(roles.values())[0])
        combo_rol.pack()
        
        def guardarCambios():
            usuario = Usuarios()    
            usuario.nombre = entry_nombre.get()
            usuario.apellido = entry_apellido.get()
            usuario.dni = entry_dni.get()
            usuario.mail = entry_mail.get()
            usuario.pwd = entry_password.get()

            for k, v in roles.items():
                if v == combo_rol.get():
                    usuario.id_rol = k
                    break
             
            respuesta = self.veridicoMail(usuario.mail)
            if respuesta[0][0] == 0:
                if usuario.pwd == entry_password_repetido.get():
                    if usuario.nombre != "" and usuario.apellido != "" and usuario.mail != "":    
                        agregar(usuario)
                        messagebox.showinfo("Éxito", "Usuario creado correctamente")
                        ventana.destroy()
                    else: messagebox.showinfo("Error", "Debe llenar los cambos Nombre, Apellido y Mail")  
                else:
                    messagebox.showerror("Error", "Las contraseñas deben ser iguales")
            else : messagebox.showwarning("Error", f"El usuario {usuario.mail} ya Existe") 
                         
        ttk.Button(ventana, text="Guardar Cambios", command=guardarCambios).pack(pady=10)    
        


    def salir(self):
        self.menuGui.destroy()

MenuUsuario()
# usuario = Clientes()
# pruebaMenu = PruebaMenu("Clientes")
# pruebaMenu.objeto = usuario
# pruebaMenu.comoBox = [('Roles',"SELECT id_rol, tipo_rol FROM roles")]
# pruebaMenu.camposIgnorados = ['id_rol']
# pruebaMenu.crearMenu()