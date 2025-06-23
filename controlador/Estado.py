from BaseDeDatos.Eda import actualizar, insertar, consultar
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def agregar(Estado):
    respuesta = insertar("Estado", **Estado.__dict__) 
    return(respuesta)

def actualiza(filtro, valorFiltro, Estado):
    actualizar("Estado", filtro, valorFiltro, **Estado.__dict__)

def consultas(query):
    return consultar(query)