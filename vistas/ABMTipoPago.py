import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controlador.TipoPago import agregar, actualiza, consultas
from modelo.TipoPago import TipoPago

def abmTipoPago():
    while True:
        print("""Selecciones una de las siguientes opciones: 
                ======================================
                |           ABM Tipo de Pago         |
                ======================================
                | 0. Salir                           |
                | 1. Agregar Tipo de Pago            |
                | 2. Modificar Tipo o Estado de Pago | 
                | 3. Listar Tipo de Pago             | 
                ======================================""")
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

def agregarTipoPago ():
    tipopago = TipoPago()
    valido4 = True
    while valido4 == True:
        desc = input ("Ingrese el tipo de pago a utilizar entre 'Debito', 'Credito' y 'Transferencia': ").strip().upper()
        if desc == 'DEBITO' or desc == 'CREDITO' or desc == 'TRANSFERENCIA':
            tipopago.descripcion = desc
            valido4 = False
        else:
            print ('El tipo de pago ingresado no es válido. Debe ingresar uno que figura en la lista.')
    valido5 = True
    while valido5 == True:
        est = input ('Ingrese A (Activo)/I (Inactivo): ').strip().upper()
        if est == 'A' or est == 'I':
            tipopago.estado = est
            valido5 = False
        else:
            print ('Debe ingresar un estado de tipo de pago válido.')
    valido6 = True
    while valido6 == True:
        confirmar = input ('¿Confirma que los datos son válidos? S (Sí)/N (No): ').strip().upper()
        if confirmar == 'S':
            respuesta = agregar (tipopago)
            valido6 = False
            print (respuesta [1])
        else:
            print ('Debe ingresar una confirmacion válida.')

def modificarTipoPago ():
    tipopago = TipoPago()
    ids_validos = []
    while True:
        try:
            consultaId = consultas (f"SELECT id_tipo_pago FROM tipo_pagos")
            for fila in consultaId:
                id_valor = fila[0]
                ids_validos.append (id_valor)
            id_TipoPago = int(input("Ingrese el id del tipo de pago a modificar: "))
            if id_TipoPago in ids_validos:
                break
            else:
                print ('El valor ingresado no corresponde con el ID de un tipo de pago existente.')
                continue
        except ValueError:
            print ('El valor ingresado no corresponde con el ID de un tipo de pago existente.')

    valido1 = True
    while valido1 == True:
        descripcion = input("Ingrese el tipo de pago entre 'Debito', 'Credito' o 'Transferencia': ").upper()
        if descripcion != "":
            if descripcion == 'TRASNFERENCIA' or descripcion == 'DEBITO' or descripcion == 'CREDITO': 
                tipopago.descripcion = descripcion
                valido1 = False
            else:
                print ('El texto ingresado no es un estado válido.')
    valido2 = True
    while valido2 == True:
        estado = input("Ingrese el estado del tipo de pago A (Activo)/I (Inactivo): ").strip().upper()
        if estado != "": 
            if estado == 'A' or estado == 'I':
                tipopago.estado = estado
                valido2 = False
        else:
            print ('El ingresar una letra entre A o I para indicar si el tipo de pago está activo o inactivo.')
    valido3 = True
    while valido3 == True:
        confirmar = input ('¿Confirma que los datos son válidos? S (Sí)/N (No): ').strip().upper()
        if confirmar == 'S' or confirmar == 'N':
            if confirmar == 'S':
                actualiza ("id_tipo_pago", id_TipoPago, tipopago)
                valido3 = False
        else:
            print ('Debe ingresar una confirmacion válida.')

def listarTipoPago ():
    consultas ('SELECT * from tipo_pagos')

abmTipoPago ()
