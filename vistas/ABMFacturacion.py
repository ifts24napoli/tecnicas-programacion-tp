import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controlador.Facturacion import agregar, actualiza, consultas
from modelo.Facturacion import Facturacion

def abmFacturacion():
    while True:
        print("""Selecciones una de las siguientes opciones: 
                ######################################
                # 0. Salir                           #
                # 1. Agregar Datos de Facturación    #
                # 2. Modificar Datos de Facturación  # 
                # 3. Listar Datos de Facturación     # 
                ######################################""")
        try: 
            opcion = int(input("Ingrese una Opción: "))
            if opcion == 0:
                break
            elif opcion == 1:
                agregarFacturacion()
            elif opcion == 2:
                modificarFacturacion()                     
            elif opcion == 3:
                listarFacturacion()
        except ValueError:
            print ("Debe ingresar un valor numérico válido.")
            continue

def verificoFacturacion():
    return consultas("Select id_facturacion, fecha_factura, monto, estado, id_contrato from facturacion")

def agregarFacturacion ():
    facturacion = Facturacion()
    facturacion.fecha_factura = input ('Ingrese la fecha de la factura: ')
    facturacion.monto = int(input('Ingrese el monto de la factura: '))
    facturacion.estado = input ('Ingrese estado de la factura P/N: ')
    facturacion.id_contrato = input ('Ingrese el ID del contrato: ')
    confirmar = input ('¿Confirma que los datos son válidos? s/n: ').upper()
    if confirmar == 'S':
        respuesta = agregar (facturacion)
        print (respuesta [1])

abmFacturacion()