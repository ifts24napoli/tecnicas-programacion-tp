from BaseDeDatos.Eda import actualizar, insertar, consultar, eleiminar
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def agregar(comodato):
    respuesta = insertar("comodato", **comodato.__dict__)
    return(respuesta)

def actualiza(filtro, valorFiltro, comodato):
    actualizar("comodato", filtro, valorFiltro, **comodato.__dict__)

def consultas(query):
    return consultar(query)

def eleiminar(filtro, valor):
    eleiminar("comodato", filtro, valor)
