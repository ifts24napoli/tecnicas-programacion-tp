import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controlador.Contratos import agregar,actualiza, consultas
from controlador.Clientes import consultas as consultasclientes
from controlador.Planes import consultas as consultasplanes
from controlador.Estado import consultas as consultasestado
from controlador.Tipo_pagos import consultas as consultaspagos
from modelo.Contratos import Contratos
from controlador.Mail import Mail

from datetime import date
def obtener_fecha_actual():
    return date.today().strftime("%Y-%m-%d")

def enviarmail (destinatario,nombre_cliente):
    mail = Mail()
    mail.asunto = "Alta de cliente"
    mail.mensaje = f""" Bienvenido {nombre_cliente} a nuestra comunidad. Para nosotros, no sos solo un cliente:
    sos parte de nuestra familia. 
    Nuestro compromiso es brindarte un servicio de telecomunicaciones confiable, 
    cercano y de calidad, construyendo juntos una relación basada en la confianza, 
    la atención personalizada y la mejora constante.
    Att Matias Napoli (Director de Ventas)"""
    mail.detinatario = destinatario
    mail.envioMail()  
    
#Funcion para validad ID
def obtener_id_valido(tabla, campo_id, mensaje, funcion_verificacion):
    while True:
        consultas(f"SELECT * FROM {tabla}")
        entrada = input(mensaje).strip()

        if not entrada.isdigit():
            print("Debe ingresar un número entero positivo válido.")
            continue

        id_valor = int(entrada)
        if id_valor <= 0:
            print("El ID debe ser un número positivo mayor que cero.")
            continue

        respuesta = funcion_verificacion(f"""SELECT {campo_id} FROM {tabla}
                                                WHERE {campo_id} = '{id_valor}'""")
        if not respuesta:
            print(f"El ID ingresado no existe en la tabla {tabla}.")
            continue

        return id_valor 


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
                BajaContrato()
            elif opcion == 3:
                ConsultarContratos()
            else:
                print("Opción no válida, ingrese un numero valido")
        except ValueError:
            print ("Debe ingresar un valos numérico")
            continue   
        

def AltaContrato():
    resultado = consultas("SELECT * FROM contratos")
    for fila in resultado:
        print(f"ID: {fila[0]}, Fecha de alta: {fila[1]}, Fecha de baja: {fila[2]}, Motivo de baja: {fila[3]}, Id Cliente: {fila[4]}, Id Plan: {fila[5]}, Id Tipo de pago: {fila[6]}, Id Estado: {fila[7]}")
    contrato = Contratos()
    print("Alta de Contrato del Sistema")

    contrato.fecha_alta = obtener_fecha_actual()

    print("Clientes registrados en la base de datos:")

    contrato.id_cliente = obtener_id_valido(
        "clientes",
        "id_clientes",
        "Ingrese el ID del cliente que desea asignar al contrato: ",
        consultasclientes
    )

    contrato.id_plan = obtener_id_valido(
        "planes",
        "id_planes",
        "Ingrese el ID del plan que desea asignar al contrato: ",
        consultasplanes
    )

    contrato.id_tipo_pago = obtener_id_valido(
        "tipo_pagos",
        "id_tipo_pago",
        "Ingrese el ID del tipo de pago que desea asignar al contrato: ",
        consultaspagos
    )

    contrato.id_estado = 1

    while True:
        opcion = input("¿Desea agregar el contrato? (s/n): ").strip().lower()
        if opcion == "s":
            insertar = agregar(contrato)
            print(insertar)

            datos = consultasclientes(f"""
                SELECT TOP 1 C.mail, CONCAT(C.nombre, ', ', C.apellido) AS NombreCompleto
                FROM contratos AS con
                INNER JOIN clientes AS C ON C.id_clientes = con.id_cliente
                WHERE C.id_clientes = {contrato.id_cliente}
            """)
            enviarmail(datos[0][0], datos[0][1])
            break
        elif opcion == "n":
            break
        else:
            print("Opción incorrecta. Intente nuevamente.")



def BajaContrato():
    resultado = consultas("SELECT * FROM contratos")
    for fila in resultado:
        print(f"ID: {fila[0]}, Fecha de alta: {fila[1]}, Fecha de baja: {fila[2]}, Motivo de baja: {fila[3]}, Id Cliente: {fila[4]}, Id Plan: {fila[5]}, Id Tipo de pago: {fila[6]}, Id Estado: {fila[7]}")
    
    contrato = Contratos()
    
    while True:
        try:
            consulta_contrato = int(input("Ingrese el id del contrato que desea dar de baja: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        respuesta = consultas(f"""SELECT * FROM contratos
                                  WHERE id_contrato = '{consulta_contrato}'""")
        if not respuesta:
            print("El ID de contrato no existe.")
            continue

        if respuesta[0][7] == 2:  # id_estado = 2 (inactivo)
            print("Este contrato ya está dado de baja (inactivo).")
            return  # Salir de la función
        
        break

    id_contrato = respuesta[0][0]
    id_cliente = respuesta[0][4]
    contrato.fecha_baja = obtener_fecha_actual()

    while True:
        motivo = input("Ingrese el motivo de baja: ").strip()
        if not motivo:
            print("El motivo de baja no puede estar vacío.")
        elif motivo.isnumeric():
            print("El motivo de baja no puede ser un número.")
        else:
            contrato.motivo_baja = motivo
            contrato.id_estado = 2
            break

    while True:
        opcion = input("¿Desea dar de baja el contrato? (s/n): ").strip().lower()
        if opcion == "s":
            modificar = actualiza("id_contrato", id_contrato, contrato)
            print("Se ha producido la baja del contrato.")
            
            # Obtener mail y nombre del cliente
            datos = consultasclientes(f"""
                SELECT C.mail, CONCAT(C.nombre, ', ', C.apellido) AS NombreCompleto
                FROM clientes AS C
                WHERE C.id_clientes = {id_cliente}
            """)
            if datos:
                mail = Mail()
                mail.asunto = "Baja de contrato"
                mail.mensaje = f""" Estimado/a {datos[0][1]},
                
Lamentamos saber que has decidido dar de baja nuestro servicio.

Queremos agradecerte sinceramente por habernos elegido y habernos permitido acompañarte durante este tiempo. 
Para nosotros, cada cliente es parte de nuestra comunidad, y tu confianza ha sido muy valiosa.

Si en el futuro decidís volver, estaremos encantados de recibirte nuevamente con los brazos abiertos. 
Nuestro compromiso sigue siendo ofrecer un servicio de calidad, cercano y humano.

Gracias por habernos permitido formar parte de tu camino.

Att. Matías Napoli (Director de Ventas)"""
                mail.detinatario = datos[0][0]
                mail.envioMail()

            break
        elif opcion == "n":
            break
        else:
            print("Opción incorrecta. Intente nuevamente.")


  

def ConsultarContratos():
    while True:
        opcion = input("¿Desea consultar la lista de contratos completa? (s/n): ").strip().lower()
        if opcion == "s":                
            resultado = consultas("SELECT * FROM contratos")
            for fila in resultado:
                print(f"ID: {fila[0]}, Fecha de alta: {fila[1]}, Fecha de baja: {fila[2]}, Motivo de baja: {fila[3]}, Id Cliente: {fila[4]}, Id Plan: {fila[5]}, Id Tipo de pago: {fila[6]}, Id Estado: {fila[7]}")
        elif opcion == "n":
            break
        else:
            print("Opción incorrecta. Intente nuevamente.")
            continue
        break
  

abmContratos()