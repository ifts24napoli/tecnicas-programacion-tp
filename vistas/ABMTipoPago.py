import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controlador.TipoPago import agregar, actualiza, consultas
from modelo.TipoPago import TipoPago

def abmTipoPago():
    while True:
        print("""Selecciones una de las siguientes opciones: 
                ######################################
                # 0. Salir                           #
                # 1. Agregar Tipo de Pago            #
                # 2. Modificar Tipo o Estado de Pago # 
                # 3. Listar Tipo de Pago             # 
                ######################################""")
        try: 
            opcion = int(input("Ingrese una Opción: "))
            if opcion == 0:
                break
            elif opcion == 1:
                agregarTipoPago()
            elif opcion == 2:
                modificarTipoPago()                     
            elif opcion == 3:
                listarTipoPago()
        except ValueError:
            print ("Debe ingresar un valor numérico")
            continue        

def verificoTipoPago():
    return consultas("Select id_tipo_pago, descripcion, estado from tipo_pagos")

def agregarTipoPago ():
    tipopago = TipoPago()
    tipopago.descripcion = input ('Ingrese el tipo de pago a utilizar: ')
    tipopago.estado = input ('Ingrese A/I: ')
    confirmar = input ('¿Confirma que los datos son válidos? s/n: ').upper()
    if confirmar == 'S':
        respuesta = agregar (tipopago)
        print (respuesta [1])

def modificarTipoPago ():
    tipopago = TipoPago()
    while True:
        id_TipoPago = int(input("Ingrese el id del tipo de pago a modificar: "))
        respuesta = consultas (f"SELECT id_tipo_pago from tipo_pagos WHERE id_tipo_pago = {id_TipoPago}")  
        if id_TipoPago is not respuesta[0] [0]:
            print ('El id ingresado no corresponde con un tipo de pago válido.')
            continue
        break
    descripcion = input("Ingrese el tipo de pago: ")
    if descripcion != "":
        tipopago.descripcion = descripcion
    estado = input("Ingrese el estado del tipo de pago A/I: ")
    if estado != "":  
        tipopago.estado = estado
    confirmar = input ('¿Confirma que los datos son válidos? s/n: ').upper()
    if confirmar == 'S':
        respuesta = actualiza ("id_tipo_pago", id_TipoPago, tipopago)

def listarTipoPago ():
    consultas ('SELECT * from tipo_pagos')

abmTipoPago ()
