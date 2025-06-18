import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controlador.Inventario import agregar,actualiza, consultas
from modelo.Inventario import Inventario

#Función de menu
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
  
     
#Funcion Ingresar inventario           
def IngresarInventario():
    inventario = Inventario()
    print("Alta de Inventario del Sistema")

    # Función para validar entrada no vacía
    def entrada_no_vacia(mensaje):
        while True:
            valor = input(mensaje).strip()
            if valor != "":
                return valor
            print("El valor no puede estar vacío. Intente nuevamente.")

    # Función  para validar enteros
    def entrada_entero(mensaje):
        while True:
            try:
                numero = int(input(mensaje))
                if numero > 0:
                    return numero
                else:
                    print("Debe ingresar un número entero positivo.")
            except ValueError:
                print("Debe ingresar un número entero válido.")

    #Carga de datos
    inventario.codigo = entrada_no_vacia("Ingrese el código del producto: ")
    inventario.descripcion = entrada_no_vacia("Ingrese la descripción: ")
    inventario.stock = entrada_entero("Ingrese el stock: ")

    #Confirmacion
    while True:
        opcion = input("¿Desea agregar el inventario? (s/n): ").lower()
        if opcion == "s":
            resultado = agregar(inventario)
            print(resultado)
            break
        elif opcion == "n":
            print("Operación cancelada.")
            break
        else:
            print("Opción incorrecta. Intente nuevamente.")
 
#Función modificar inventario  
def modificarInventario():
    resultado = consultas("SELECT id_inventario, codigo, descripcion, stock FROM inventario")
    for fila in resultado:
        print(f"ID: {fila[0]}, Código: {fila[1]}, Descripción: {fila[2]}, Stock: {fila[3]}")
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
    
    descripcion = input("Ingrese la descripción (Enter para mantener actual): ")
    if descripcion != "":  
        inventario.descripcion = descripcion
    
    while True:
        stock = input("Ingrese el stock (Enter para mantener actual): ")
        if stock == "":
            inventario.stock = respuesta[0][3]
            break
        try:
            stock_int = int(stock)
            if stock_int > 0:
                inventario.stock = stock_int
                break
            else:
                print("El stock debe ser un número entero positivo.")
        except ValueError:
            print("Stock inválido. Ingrese un número entero positivo o presione Enter para mantener el actual.")

    modificar = actualiza("id_inventario", id_inventario, inventario)

  
#Función Consultar Inventario  
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
