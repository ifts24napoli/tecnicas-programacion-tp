import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controlador.Contratos import agregar,actualiza, consultas
from controlador.Clientes import consultas as consultasclientes
from controlador.Planes import consultas as consultasplanes
from controlador.Estado import consultas as consultasestado
from controlador.Tipo_pagos import consultas as consultaspagos
from modelo.Contratos import Contratos



from datetime import date
def obtener_fecha_actual():
    return date.today()

#fecha_hoy = obtener_fecha_actual()


def abmContratos():
    while True:
        print("""Selecciones una de las siguientes opciones: 
                #############################
                # 0. Salir                  #
                # 1. Alta de Contrato       #
                # 2. Baja de Contrato       # 
                # 3. Consultar Contratos    # 
                #############################""")
        try: 
            opcion = int(input("Ingrese una Opción: "))
            if opcion == 0:
                break
            elif opcion == 1:
                AltaContrato()
            elif opcion == 2:
                #BajaContrato()
            #elif opcion == 3:
                #ConsultarContrato()
            #else:
                print("Opción no válida, ingrese un numero valido")
        except ValueError:
            print ("Debe ingresar un valos numérico")
            continue   
        
def AltaContrato():
    consultas("select * from contratos")
    contrato = Contratos()
    print("Alta de Contrato del Sistema")
    while True:
        try:
            contrato.id_contrato = int(input("Ingrese el ID del contrato: "))
            if contrato.id_contrato > 0:
                break
            else:
                print("El ID del contrato debe ser un número entero positivo.")
        except ValueError:
            print("Debe ingresar un número entero válido.")
    
    contrato.fecha_alta = obtener_fecha_actual()
    #contrato.fecha_alta = '2025-06-19'
    print (contrato.fecha_alta)
    
    while True:
        consultas("select * from clientes")
        consulta_idCliente =int (input("Ingrese el id del cliente que desea asignar el contrato: "))
        respuesta = consultasclientes(f"""Select id_clientes from clientes
                          where id_clientes = '{consulta_idCliente}'""")
        if not respuesta:
            print("El ID del cliente no existe.")
            continue 
        break
    contrato.id_cliente= consulta_idCliente
    
    while True:
        consultas("select * from planes")
        consulta_planes =int (input("Ingrese el id del plan que desea asignar a el contrato: "))
        respuesta = consultasplanes(f"""Select id_planes from planes
                          where id_planes = '{consulta_planes}'""")
        if not respuesta:
            print("El ID del cliente no existe.")
            continue 
        break
    contrato.id_plan= consulta_planes
    
  

    
    while True:
            opcion = input("¿Desea agregar el contrato? (s/n): ").strip().lower()
            if opcion == "s":                
                insertar = agregar(contrato)
                print(insertar) 
            elif opcion == "n":
                break
            else:
                print("Opción incorrecta. Intente nuevamente.")
                continue
            break
    
    
    
     

    
abmContratos()




