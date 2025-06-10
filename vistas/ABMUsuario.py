import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controlador.Usuarios import agregar,actualiza, consultas
from controlador.Roles import consultas as consultasRol
from modelo.Usuarios import Usuarios
from modelo.Roles import Roles

# usuarios = Usuarios(Nombre = "Pepesssss", Apellido = "otssssro", Id_rol = 1, Mail = "otro@gmail.com")
# agregar(usuarios)

# usuarios = Usuarios(Nombre = "Roxana")
# actualiza("id_usuario", 10, usuarios)

# consultar("""Select U.nombre, U.apellido, tipo_rol
#           from usuarios as U
#           inner join roles On roles.id_rol = U.id_rol""")
def abmUsuarios():
    while True:
        print("""Selecciones una de las siguientes opciones: 
                ##########################
                # 0. Salir               #
                # 1. Crear Usuario       #
                # 2. Modificar Usuario   #  
                # 3. Eliminar Usuario    #
                ##########################""")
        
        opcion = int(input("Ingrese una Opción: "))
        if opcion == 0:
            break
        elif opcion == 1:
            usuarioNuevo()

def verificoRol():
    consultasRol("Select id_rol, tipo_rol from roles")
    
                
def usuarioNuevo():
    usuarios = Usuarios()
    print("Alta de Usuarios del Sistema")
    usuarios.nombre = input("Ingrese Nombre del Usuario: ")
    usuarios.apellido = input("Ingrese Apellido del Apellido: ")
    usuarios.mail = input("Ingrese Mail: ")
    verificoRol()
    usuarios.id_rol = int(input("Selecione un Rol ID: "))
    # usuarios.id_rol = 1 # Hay que mostrar las diferentes opciones
    respuesta =  agregar(usuarios)
    print(respuesta[1]) # En la posición 1 muestra el mensaje, en la 0 muestra el # del id del registro creado
    
        