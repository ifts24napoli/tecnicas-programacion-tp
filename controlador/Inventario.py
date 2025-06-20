from BaseDeDatos.Eda import actualizar, insertar, consultar
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def agregar(inventario):
    respuesta = insertar("inventario", **inventario.__dict__) #**alumnos.__dict__ convierto el objeto a Diccionario
    return(respuesta)

def actualiza(filtro, valorFiltro, inventario):
    actualizar("inventario", filtro, valorFiltro, **inventario.__dict__)

"""Necesito algo asi para actualizar la cantidad de comodato en base al stock del inventario:

def actualizar_stock(id_inventario, nuevo_stock):
    actualizar("inventario", "id_inventario", id_inventario, stock=nuevo_stock)"""

def consultas(query):
    return consultar(query)
    