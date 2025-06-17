import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controlador.Inventario import agregar,actualiza, consultas
from modelo.Inventario import Inventario

def abmInventario():
    while True:
        print("""Selecciones una de las siguientes opciones: 
                #############################
                # 0. Salir                  #
                # 1. Ingresar Inventario    #
                # 2. Modificar Inventario   # 
                # 3. Consultar Inventario   # 
                #############################""")
        try: 
            opcion = int(input("Ingrese una Opción: "))
            if opcion == 0:
                break
            elif opcion == 1:
                IngresarInventario()
            elif opcion == 2:
                modificarInventario()
            elif opcion == 3:
                consultarInventario()
            else:
                print("Opción no válida, ingrese un numero valido")
        except ValueError:
            print ("Debe ingresar un valos numérico")
            continue   
            
            
            
def IngresarInventario():
    inventario = Inventario()
    print("Alta de Inventario del Sistema")
    inventario.codigo = input("Ingrese el código del producto: ")
    inventario.descripcion = input("Ingrese la descripción: ")

    while True:
        try:
            inventario.stock = int(input("Ingrese el stock: "))
            break
        except ValueError:
            print("Debe ingresar un número entero para el stock.")

    while True:
        opcion = input("¿Desea agregar el inventario? (s/n): ").strip().lower()
        if opcion == "s":                
            insertar = agregar(inventario)
            print(insertar) 
        elif opcion == "n":
            break
        else:
            print("Opción incorrecta. Intente nuevamente.")
            continue
        break
      
  
   
def modificarInventario():
    consultas("select * from inventario")
    inventario = Inventario()
    while True:
        consulta_inventario =int (input("Ingrese el id del inventario que desea modificar: "))
        respuesta = consultas(f"""Select id_inventario, codigo, descripcion, stock from inventario
                                where id_inventario = '{consulta_inventario}'""")
        if not respuesta:
            print("El ID de inventario no existe.")
            continue 
        break
    
    id_inventario = respuesta[0][0]
    codigo = input("Ingrese el código (Enter para mantener actual): ")
    if codigo != "":
        inventario.codigo = codigo
    else:
        inventario.codigo = respuesta[0][1]

    descripcion = input("Ingrese la descripción (Enter para mantener actual): ")
    if descripcion != "":  
        inventario.descripcion = descripcion
    else:
        inventario.descripcion = respuesta[0][2]

    stock = input("Ingrese el stock (Enter para mantener actual): ")   
    if stock != "":
        try:
            inventario.stock = int(stock)
        except ValueError:
            print("Stock inválido, se mantiene el valor anterior.")
            inventario.stock = respuesta[0][3]
    else:
        inventario.stock = respuesta[0][3] 

    modificar = actualiza("id_inventario", id_inventario, inventario)
    
   

def consultarInventario():
    while True:
        opcion = input("¿Desea consultar el inventario completo? (s/n): ").strip().lower()
        if opcion == "s":                
            resultado = consultas("SELECT id_inventario, codigo, descripcion, stock FROM inventario")
            for fila in resultado:
                print(f"ID: {fila[0]}, Código: {fila[1]}, Descripción: {fila[2]}, Stock: {fila[3]}")
        elif opcion == "n":
            break
        else:
            print("Opción incorrecta. Intente nuevamente.")
            continue
        break
  

abmInventario()
