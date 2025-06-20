from BaseDeDatos.Eda import actualizar, insertar, consultar
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def agregar(planes):
    respuesta = insertar("planes", **planes.__dict__) #**alumnos.__dict__ convierto el objeto a Diccionario
    return(respuesta)

def actualiza(filtro, valorFiltro, planes):
    actualizar("planes", filtro, valorFiltro, **planes.__dict__)

def consultas(query):
    return consultar(query)