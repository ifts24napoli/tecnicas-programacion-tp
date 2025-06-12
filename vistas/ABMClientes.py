import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controlador.Clientes import agregar,actualiza, consultas
from controlador.Roles import consultas as consultasRol
from modelo.Clientes import Clientes

def abmClientes():
    while True:
        print("""Selecciones una de las siguientes opciones: 
                ##########################
                # 0. Salir               #
                # 1. Crear Cliente       #
                # 2. Modificar Cliente   # 
                # 3. Lista de Clientes   # 
                # 4. Eliminar Cliente    #
                ##########################""")
        try: 
            opcion = int(input("Ingrese una Opción: "))
            if opcion == 0:
                break
            elif opcion == 1:
                clienteNuevo()
            elif opcion == 2:
                modificarCliente()
            elif opcion == 3:
                listarClientes()
            elif opcion == 4:
                eliminarCliente()
        except ValueError:
            print ("Debe ingresar un valos numérico")
            continue        
                        

def verificoRol():
    return consultasRol("Select id_rol, tipo_rol from roles")
    
                
def clienteNuevo():
    clientes = Clientes()
    print("Alta de Clientes del Sistema")
    clientes.nombre = input("Ingrese Nombre del cliente: ")
    clientes.apellido = input("Ingrese Apellido del Apellido: ")
    clientes.mail = input("Ingrese Mail: ")
    respuesta = dict(verificoRol())
    while True:
        clientes.id_rol = int(input("Selecione un Rol ID: "))
        if clientes.id_rol in respuesta:
        # cliente.id_rol = 1 # Hay que mostrar las diferentes opciones
            confirmación = input("Confirma el cambio s/n? ") 
            if confirmación.lower() == "s":
                respuesta =  agregar(clientes)
                print(respuesta[1]) # En la posición 1 muestra el mensaje, en la 0 muestra el # del id del registro creado
            else: print ("No se guardaron los cambios")
            break
        print ("Debe seleccionar un ID Rol de la lista")
        continue
        
def modificarCliente():
    cliente = Clientes()
    while True:
        mail = input("Ingrese el mail del usuario a modificar: ")
        respuesta = consultas(f"""Select U.id_cliente, U.nombre, U.apellido, U.dni, U.Mail , R.tipo_rol from usuarios as U
                                inner join roles as R ON R.id_rol = U.id_rol
                                where mail = '{mail}'""")
        if not respuesta:
            print("El cliente no existe")
            continue 
        break
    id_cliente = respuesta[0][0]
    nombre = input("Ingrese el nombre: ")
    if nombre != "":
        cliente.nombre = nombre
    apellido = input("Ingrese el apellido: ")
    if apellido != "":  
        cliente.apellido = apellido
    dni = input("Ingrese DNI: ")   
    if dni != "":
        cliente.dni = dni 
    mail = input("Ingrese el mail: ")
    if mail != "":
        cliente.mail = mail 
    respuestaRol = dict(verificoRol())
    while True:
        cliente.id_rol = int(input("Selecione un Rol ID: "))
        if cliente.id_rol in respuestaRol:  
            confirmación = input("Confirma el cambio s/n? ") 
            if confirmación.lower() == "s":
                actualiza("id_cliente", id_cliente, cliente)
            break
        print ("Debe seleccionar un ID Rol de la lista")
        continue
        
    # actualiza("cliente_id", 10, cliente)
       
        
def listarClientes():
    consultas("""Select C.cli, C.nombre, C.apellido, C.dni, C.Mail , R.tipo_rol from clientes as U
                inner join roles as R ON R.id_rol = U.id_rol""")
    
def eliminarCliente():
    print("Elimino Cliente")   