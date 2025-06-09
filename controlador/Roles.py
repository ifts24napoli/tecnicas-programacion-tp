from BaseDeDatos.Eda import actualizar, insertar, consultar
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def agregar(roles):
    respuesta = insertar("roles", **roles.__dict__)
    return(respuesta)

def actualiza(filtro, valorFiltro, usuarios):
    actualizar("roles", filtro, valorFiltro, **usuarios.__dict__)

def consultas(query):
    consultar(query)