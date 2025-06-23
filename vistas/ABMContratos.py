import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controlador.Contratos import agregar,actualiza, consultas
from controlador.Clientes import consultas as consultasclientes
from controlador.Planes import consultas as consultasplanes
from controlador.Estado import consultas as consultasestado
from controlador.Tipo_pagos import consultas as consultaspagos
from modelo.Contratos import Contratos
from controlador.Mail import Mail

#Funcion para sacar fecha actual.
from datetime import date
def obtener_fecha_actual():
    return date.today().strftime("%Y-%m-%d")

#Funcion para enviar Mail.
def enviarmail (destinatario,asunto,mensaje):
    mail = Mail()
    mail.asunto = asunto
    mail.mensaje = mensaje
    mail.detinatario = destinatario
    mail.envioMail()  
    
#Funcion para validar ID.
def obtener_id_valido(tabla, campo_id, mensaje, funcion_verificacion,tipoestado):
    print(f"\nRegistros disponibles en la tabla {tabla}:")
    if tipoestado =="verificarestado":
        registros = funcion_verificacion(f"SELECT * FROM {tabla} where estado = 'Activo'")
    else:
        registros = funcion_verificacion(f"SELECT * FROM {tabla}")
    
    for fila in registros:
        print(" | ".join(str(col) for col in fila))
    print() 

    while True:
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

#Funcion Munu Contratos:
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
        
#Funcion Alta Contrato.
def AltaContrato():
  
    resultado = consultas("""SELECT C.*, E.*, concat (Cli.nombre,', ',Cli.apellido) as Nombre , P.*,T.* FROM contratos as C
                          inner join estados as E on E.Id_estados =C.Id_estado
                          inner join clientes as Cli on Cli.id_clientes = C.id_cliente
                          inner join planes as P on P.id_planes = C.id_plan
                          inner join tipo_pagos as T on T.id_tipo_pago = C.id_tipo_pago """)
    for fila in resultado:
        print(f"ID: {fila[0]} | Fecha de alta: {fila[1]} | Fecha de baja: {fila[2]} | Motivo de baja: {fila[3]} | Cliente: {fila[11]} | Plan: {fila[13]} | Tipo de pago: {fila[16]} | Estado: {fila[9]}")

    contrato = Contratos()
    print("Alta de Contrato del Sistema")

    contrato.fecha_alta = obtener_fecha_actual()

    contrato.id_cliente = obtener_id_valido(
        "clientes",
        "id_clientes",
        "Ingrese el ID del cliente que desea asignar al contrato: ",
        consultasclientes,
        "verificar"
    )

    contrato.id_plan = obtener_id_valido(
        "planes",
        "id_planes",
        "Ingrese el ID del plan que desea asignar al contrato: ",
        consultasplanes,
        "verificar"
    )

    contrato.id_tipo_pago = obtener_id_valido(
        "tipo_pagos",
        "id_tipo_pago",
        "Ingrese el ID del tipo de pago que desea asignar al contrato: ",
        consultaspagos,
        "verificarestado"
    )
    contrato.id_estado = 1
    
    #Confirmar Alta.
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
            ASUNTO= "Alta de cliente"
            MENSAJE = f""" Bienvenido {datos[0][1]} a nuestra comunidad. Para nosotros, no sos solo un cliente:
            sos parte de nuestra familia. 
            Nuestro compromiso es brindarte un servicio de telecomunicaciones confiable, 
            cercano y de calidad, construyendo juntos una relación basada en la confianza, 
            la atención personalizada y la mejora constante.
            Att Matias Napoli (Director de Ventas)"""
            enviarmail(datos[0][0],ASUNTO,MENSAJE)
            break
        elif opcion == "n":
            break
        else:
            print("Opción incorrecta. Intente nuevamente.")


#Funcion Baja Contrato.
def BajaContrato():
    resultado = consultas("""SELECT C.*, E.*, concat (Cli.nombre,', ',Cli.apellido) as Nombre , P.*,T.* FROM contratos as C
                          inner join estados as E on E.Id_estados =C.Id_estado
                          inner join clientes as Cli on Cli.id_clientes = C.id_cliente
                          inner join planes as P on P.id_planes = C.id_plan
                          inner join tipo_pagos as T on T.id_tipo_pago = C.id_tipo_pago """)
    for fila in resultado:
        print(f"ID: {fila[0]} | Fecha de alta: {fila[1]} | Fecha de baja: {fila[2]} | Motivo de baja: {fila[3]} | Cliente: {fila[11]} | Plan: {fila[13]} | Tipo de pago: {fila[16]} | Estado: {fila[9]}")

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

        if respuesta[0][7] == 2:  
            print("Este contrato ya está dado de baja (inactivo).")
            continue  
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
    
    #Confirmar Baja.
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
                ASUNTO= "Baja de contrato"
                MENSAJE = f""" Estimado/a {datos[0][1]},
                
                Lamentamos saber que has decidido dar de baja nuestro servicio.

                Queremos agradecerte sinceramente por habernos elegido y habernos permitido acompañarte durante este tiempo. 
                Para nosotros, cada cliente es parte de nuestra comunidad, y tu confianza ha sido muy valiosa.

                Si en el futuro decidís volver, estaremos encantados de recibirte nuevamente con los brazos abiertos. 
                Nuestro compromiso sigue siendo ofrecer un servicio de calidad, cercano y humano.

                Gracias por habernos permitido formar parte de tu camino.

                Att. Matías Napoli (Director de Ventas)"""
                enviarmail(datos[0][0],ASUNTO,MENSAJE)

            break
        elif opcion == "n":
            break
        else:
            print("Opción incorrecta. Intente nuevamente.")


#Funcion Consulta Contrato.
def ConsultarContratos():
    while True:
        opcion = input("¿Desea consultar la lista de contratos completa? (s/n): ").strip().lower()
        if opcion == "s":                
            resultado = consultas("""SELECT C.*, E.*, concat (Cli.nombre,', ',Cli.apellido) as Nombre , P.*,T.* FROM contratos as C
                          inner join estados as E on E.Id_estados =C.Id_estado
                          inner join clientes as Cli on Cli.id_clientes = C.id_cliente
                          inner join planes as P on P.id_planes = C.id_plan
                          inner join tipo_pagos as T on T.id_tipo_pago = C.id_tipo_pago """)
            for fila in resultado:
                print(f"ID: {fila[0]} | Fecha de alta: {fila[1]} | Fecha de baja: {fila[2]} | Motivo de baja: {fila[3]} | Cliente: {fila[11]} | Plan: {fila[13]} | Tipo de pago: {fila[16]} | Estado: {fila[9]}")
        elif opcion == "n":
            break
        else:
            print("Opción incorrecta. Intente nuevamente.")
            continue
        break
  

abmContratos()