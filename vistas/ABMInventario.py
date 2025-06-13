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
            #elif opcion == 2:
                #modificarInventario()
            #elif opcion == 3:
                #consultarInventario()
        except ValueError:
            print ("Debe ingresar un valos numérico")
            continue   
            
            
            
def IngresarInventario():
    inventario = Inventario()
    print("Alta de Inventario del Sistema")
    inventario.codigo = input("Ingrese el codigo del producto: ")
    inventario.descripcion = input("Ingrese la descripcion: ")
    inventario.stock = int(input("Ingrese el stock: "))
    print (inventario.codigo)
    insertar =  agregar(Inventario)
    print(insertar) 
    
#def ModificarInventario():
#def ConsultarInventario():

abmInventario()
