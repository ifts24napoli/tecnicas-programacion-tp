from BaseDeDatos.Eda import actualizar, insertar, consultar
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def agregar(inventario):
    respuesta = insertar("inventario", **inventario.__dict__) #**alumnos.__dict__ convierto el objeto a Diccionario
    return(respuesta)

def actualiza(filtro, valorFiltro, inventario):
    actualizar("inventario", filtro, valorFiltro, **inventario.__dict__)

def consultas(query):
    return consultar(query)
    