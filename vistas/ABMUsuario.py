import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controlador.Usuarios import agregar,actualiza, consultas
from controlador.Roles import consultas as consultasRol
from modelo.Usuarios import Usuarios

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
                # 3. Lista de Usuarios   # 
                # 4. Eliminar Usuario    #
                ##########################""")
        try: 
            opcion = int(input("Ingrese una Opción: "))
            if opcion == 0:
                break
            elif opcion == 1:
                usuarioNuevo()
            elif opcion == 2:
                modificarUsuario()
            elif opcion == 3:
                listarUsuarios()
            elif opcion == 4:
                eliminarUsuario()
        except ValueError:
            print ("Debe ingresar un valos numérico")
            continue        
                        

def verificoRol():
    return consultasRol("Select id_rol, tipo_rol from roles")
    
                
def usuarioNuevo():
    usuarios = Usuarios()
    print("Alta de Usuarios del Sistema")
    usuarios.nombre = input("Ingrese Nombre del Usuario: ")
    usuarios.apellido = input("Ingrese Apellido del Apellido: ")
    usuarios.mail = input("Ingrese Mail: ")
    respuesta = dict(verificoRol())
    while True:
        usuarios.id_rol = int(input("Selecione un Rol ID: "))
        if usuarios.id_rol in respuesta:
        # usuarios.id_rol = 1 # Hay que mostrar las diferentes opciones
            confirmación = input("Confirma el cambio s/n? ") 
            if confirmación.lower() == "s":
                respuesta =  agregar(usuarios)
                print(respuesta[1]) # En la posición 1 muestra el mensaje, en la 0 muestra el # del id del registro creado
            else: print ("No se guardaron los cambios")
            break
        print ("Debe seleccionar un ID Rol de la lista")
        continue
        
def modificarUsuario():
    usuario = Usuarios()
    while True:
        mail = input("Ingrese el mail del usuario a modificar: ")
        respuesta = consultas(f"""Select U.id_usuario, U.nombre, U.apellido, U.dni, U.Mail , R.tipo_rol from usuarios as U
                                inner join roles as R ON R.id_rol = U.id_rol
                                where mail = '{mail}'""")
        if not respuesta:
            print("El cliente no existe")
            continue 
        break
    id_usuario = respuesta[0][0]
    nombre = input("Ingrese el nombre: ")
    if nombre != "":
        usuario.nombre = nombre
    apellido = input("Ingrese el apellido: ")
    if apellido != "":  
        usuario.apellido = apellido
    dni = input("Ingrese DNI: ")   
    if dni != "":
        usuario.dni = dni 
    mail = input("Ingrese el mail: ")
    if mail != "":
        usuario.mail = mail 
    respuestaRol = dict(verificoRol())
    while True:
        usuario.id_rol = int(input("Selecione un Rol ID: "))
        if usuario.id_rol in respuestaRol:  
            confirmación = input("Confirma el cambio s/n? ") 
            if confirmación.lower() == "s":
                actualiza("id_usuario", id_usuario, usuario)
            break
        print ("Debe seleccionar un ID Rol de la lista")
        continue
        
    # actualiza("usuario_id", 10, usuario)
       
        
def listarUsuarios():
    consultas("""Select U.id_usuario, U.nombre, U.apellido, U.dni, U.Mail , R.tipo_rol from usuarios as U
                inner join roles as R ON R.id_rol = U.id_rol""")
    
def eliminarUsuario():
    print("Elimino Usuario")   
