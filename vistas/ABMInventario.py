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
        except ValueError:
            print ("Debe ingresar un valos numérico")
            continue   
            
            
            
def IngresarInventario():
    inventario = Inventario()
    print("Alta de Inventario del Sistema")
    inventario.codigo = input("Ingrese el codigo del producto: ")
    inventario.descripcion = input("Ingrese la descripcion: ")
    inventario.stock = int(input("Ingrese el stock: "))
    insetar =  agregar(inventario)
    print(insetar) 
    
def modificarInventario():
    inventario = Inventario()
    while True:
        consulta_inventario =int (input("Ingrese el id del inventario que desea modificar: "))
        respuesta = consultas(f"""Select id_inventario, codigo, descripcion, stock from inventario
                                where id_inventario = '{consulta_inventario}'""")
        if not respuesta:
            print("El id inventario no existe")
            continue 
        break
    id_inventario = respuesta[0][0]
    codigo = input("Ingrese el codigo: ")
    if codigo != "":
        inventario.codigo = codigo
    descripcion = input("Ingrese la descripcion: ")
    if descripcion != "":  
        inventario.descripcion= descripcion
    stock = input("Ingrese el stock: ")   
    if stock != "":
        inventario.stock = stock 
    modificar = actualiza("id_inventario",id_inventario,inventario)
   

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
