import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controlador.Clientes import agregar,actualiza, consultas
from modelo.Clientes import Clientes

# usuarios = Usuarios(Nombre = "Pepesssss", Apellido = "otssssro", Id_rol = 1, Mail = "otro@gmail.com")
# agregar(usuarios)

# usuarios = Usuarios(Nombre = "Roxana")
# actualiza("id_usuario", 10, usuarios)

# consultar("""Select U.nombre, U.apellido, tipo_rol
#           from usuarios as U
#           inner join roles On roles.id_rol = U.id_rol""")
def abmClientes():
    while True:
        print("""Selecciones una de las siguientes opciones: 
                ##########################
                # 0. Salir               #
                # 1. Crear Clientes       #
                # 2. Modificar Clientes   #  
                # 3. Eliminar Clientes    #
                ##########################""")
        
        opcion = int(input("Ingrese una Opción: "))
        if opcion == 0:
            break
        elif opcion == 1:
            clienteNuevo()
            
def clienteNuevo():
    clientes = Clientes()
    print("Alta de clientes del Sistema")
    clientes.nombre = input("Ingrese Nombre del Clientes: ")
    clientes.apellido = input("Ingrese Apellido del Cliente: ")
    clientes.mail = input("Ingrese Mail: ")
    respuesta =  agregar(clientes)
    print(respuesta[1]) # En la posición 1 muestra el mensaje, en la 0 muestra el # del id del registro creado
    
        