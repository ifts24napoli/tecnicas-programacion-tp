from BaseDeDatos.Eda import actualizar, insertar, consultar
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def agregar(usuarios):
    respuesta = insertar("usuarios", **usuarios.__dict__) #**alumnos.__dict__ convierto el objeto a Diccionario
    return(respuesta)

def actualiza(filtro, valorFiltro, usuarios):
    actualizar("usuarios", filtro, valorFiltro, **usuarios.__dict__)

def consultas(query):
    consultar(query)