import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controlador.Facturacion import agregar, actualiza, consultas
from modelo.Facturacion import Facturacion
from controlador.Contratos import consultas as consultaContratos
from datetime import date

def abmFacturacion():
    while True:
        print("""Selecciones una de las siguientes opciones: 
                ======================================
                |           ABM Facturación          |
                ======================================
                | 0. Salir                           |
                | 1. Agregar Datos de Facturación    |
                | 2. Modificar Datos de Facturación  | 
                | 3. Listar Datos de Facturación     | 
                ======================================""")
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

def agregarFacturacion ():
    facturacion = Facturacion()
    valido4 = True
    valido5 = True

    contratos = consultaContratos("SELECT c.id_contrato, CONCAT(cli.nombre, ', ', cli.apellido) AS cliente FROM contratos AS c INNER JOIN clientes AS cli ON cli.id_clientes = c.id_cliente")
    print("Contratos disponibles:")
    for c in contratos:
        print(f"ID: {c[0]} - Cliente: {c[1]}") 
    while True:
        try:
            id_contrato = int(input("Ingrese el ID del contrato elegido: "))
            contratos = dict (contratos)
            if id_contrato in contratos:
                facturacion.id_contrato = id_contrato
                break
            else:
                print ('El ID del contrato seleccionado no existe.')
        except ValueError:
            print ('El ID debe ser un valor numérico existente en la lista.')
            continue
    respuesta = consultas(f"SELECT p.precio FROM planes AS p INNER JOIN contratos AS c ON p.id_planes = c.id_plan WHERE c.id_contrato = {facturacion.id_contrato}")
    facturacion.monto = float(respuesta [0][0])
    facturacion.fecha_factura = date.today().strftime("%Y-%m-%d")
    
    while valido4 == True:
        estado_factura = input("Ingrese estado de la factura P (Paga)/I (Inpaga)/C (Cancelada): ").strip().upper()
        if estado_factura == 'P' or estado_factura == 'I' or estado_factura == 'C':
            if estado_factura == 'P':
                facturacion.estado = 'PAGA'
            if estado_factura == 'I':
                facturacion.estado = 'INPAGA'
            if estado_factura == 'C':
                facturacion.estado = 'CANCELADA'
            valido4 = False
        else:
            print ('El estado de factura ingresado no es válido. Debe ingresar P (Paga)/I (Inpaga)/C (Cancelada)')
    
    while valido5 == True:
        confirmar = input("¿Confirma que los datos son válidos? S (Sí)/N (No): ").strip().upper()
        if confirmar == 'S' or confirmar == 'N':
            if confirmar == 'S':
                respuesta = agregar(facturacion)
            valido5 = False
                
def modificarFacturacion ():
    facturacion = Facturacion()
    ids_validos = []
    listado = consultas("""SELECT f.id_facturacion, f.fecha_factura, f.monto, f. estado, c.id_contrato, CONCAT(cli.nombre, ', ', cli.apellido) AS cliente 
                        FROM facturacion AS f
                        INNER JOIN contratos AS c ON c.id_contrato = f.id_contrato 
                        INNER JOIN clientes AS cli ON cli.id_clientes = c.id_cliente""")
    for con in listado:
        print(f"ID: {con[0]} - Fecha de facturación: {con[1]} - Monto {con[2]} - Estado: {con[3]} - ID del Contrato: {con[4]} - Cliente: {con[5]}")
    consultaId = consultas ('SELECT id_facturacion FROM facturacion')
    for fila in consultaId:
        id_valor = fila [0]
        ids_validos.append (id_valor)
    while True:
        try:
            id_Facturacion = int(input("Ingrese el id de la factura a modificar: "))
            if id_Facturacion in ids_validos:
                break
            else:
                print ('El id ingresado no corresponde con una factura existente.')
                continue
            break
        except ValueError:
            print ('El ID ingresado debe ser un valor entero.')

    facturacion.fecha_factura = date.today().strftime("%Y-%m-%d")
    
    valido2 = True
    while valido2 == True:
            estado = input("Ingrese el estado de la factura: P (Paga))/I (Inpaga)/ C (Cancelada): ").strip().upper()
            if estado != "":
                if estado == 'P' or estado == 'I' or estado == 'C':
                    if estado == 'P':
                        facturacion.estado = 'PAGA'
                    if estado == 'I':
                        facturacion.estado = 'INPAGA'
                    if estado == 'C':
                        facturacion.estado = 'CANCELADA'
                    valido2 = False
                else:
                    print ('El texto ingresado no es un estado válido.')
            else:
                valido2 = False
    valido3 = True
    while valido3 == True:
        confirmar = input ('¿Confirma que los datos son válidos? S (Sí)/N (No): ').strip().upper()
        if confirmar == 'S' or confirmar == 'N':
            if confirmar == 'S':
                actualiza ("id_facturacion", id_Facturacion, facturacion)
            valido3 = False
        else:
            print ('Para confirmar debe ingresar S, en caso afirmativo, o N en caso negativo.')


def listarFacturacion ():
    listado = consultas("""SELECT f.id_facturacion, f.fecha_factura, f.monto, f. estado, c.id_contrato, CONCAT(cli.nombre, ', ', cli.apellido) AS cliente 
                        FROM facturacion AS f
                        INNER JOIN contratos AS c ON c.id_contrato = f.id_contrato 
                        INNER JOIN clientes AS cli ON cli.id_clientes = c.id_cliente""")
    for con in listado:
        print(f"ID: {con[0]} - Fecha de facturación: {con[1]} - Monto {con[2]} - Estado: {con[3]} - ID del Contrato: {con[4]} - Cliente: {con[5]}")

# abmFacturacion()