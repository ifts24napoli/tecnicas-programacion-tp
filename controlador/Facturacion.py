from BaseDeDatos.Eda import actualizar, insertar, consultar
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def agregar(facturacion):
    respuesta = insertar("facturacion", **facturacion.__dict__) #El objeto facturacion a diccionario
    return(respuesta)

def actualiza(filtro, valorFiltro, facturacion):
    actualizar("facturacion", filtro, valorFiltro, **facturacion.__dict__)

def consultas(query):
    return consultar(query)