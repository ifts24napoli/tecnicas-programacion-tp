import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controlador.Facturacion import agregar, actualiza, consultas
from modelo.Facturacion import Facturacion
from controlador.Contratos import consultas as consultaContratos

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
    contratos = consultaContratos("SELECT id_contrato, id_cliente FROM contratos")
    print("Contratos disponibles:")
    for c in contratos:
        print(f"ID: {c[0]} - Cliente: {c[1]}")
    facturacion.id_contrato = input("Ingrese el ID del contrato elegido: ")
    facturacion.monto = consultas(f"SELECT p.precio FROM planes AS p INNER JOIN contratos AS c ON p.id_plan = c.id_plan WHERE c.id_contrato = '{facturacion.id_contrato}")
    facturacion.fecha_factura = input("Ingrese la fecha de la factura: ")
    facturacion.estado = input("Ingrese estado de la factura P/N: ").upper()
    confirmar = input("¿Confirma que los datos son válidos? s/n: ").upper()
    if confirmar == 'S':
        respuesta = agregar(facturacion)
        print(respuesta[1])

def listarFacturacion ():
    return consultas ("SELECT * FROM facturacion")

abmFacturacion()