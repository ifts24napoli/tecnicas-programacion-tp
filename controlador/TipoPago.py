from BaseDeDatos.Eda import actualizar, insertar, consultar
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def agregar(tipopago):
    respuesta = insertar("tipo_pagos", **tipopago.__dict__) #El objeto tipopago a diccionario
    return(respuesta)

def actualiza(filtro, valorFiltro, tipopago):
    actualizar("tipo_pagos", filtro, valorFiltro, **tipopago.__dict__)

def consultas(query):
    return consultar(query)