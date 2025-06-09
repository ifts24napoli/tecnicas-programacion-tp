import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controlador.Usuarios import agregar,actualiza, consultar
from modelo.Usuarios import Usuarios

# usuarios = Usuarios(Nombre = "Pepesssss", Apellido = "otssssro", Id_rol = 1, Mail = "otro@gmail.com")
# agregar(usuarios)
# usuarios = Usuarios(Nombre = "Roxana")
# actualiza("id_usuario", 10, usuarios)
# consultar("""Select U.nombre, U.apellido, tipo_rol
#           from usuarios as U
#           inner join roles On roles.id_rol = U.id_rol""")
def abm():
    while True:
        print("""Selecciones una de las siguientes opciones: \n 
                 0. Salir   
                 1. Crear Usuario
                 2. Modificar Usuario
                 3. Eliminar Usuario""")
        opcion = int(input("Ingrese una Opción: "))
        if opcion == 0:
            break
        elif opcion == 1:
            usuarioNuevo()
            
def usuarioNuevo():
    usuarios = Usuarios()
    print("Alta de Usuarios del Sistema")
    usuarios.nombre = input("Ingrese Nombre del Usuario: ")
    usuarios.apellido = input("Ingrese Apellido del Apellido: ")
    usuarios.mail = input("Ingrese Mail: ")
    usuarios.id_rol = 1
    respuesta =  agregar(usuarios)
    print(respuesta[1]) #En la posición 1 muestra el mensaje, en la 0 muestra el # del id del registro creado
    
        