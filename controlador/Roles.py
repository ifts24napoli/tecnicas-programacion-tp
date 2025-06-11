from BaseDeDatos.Eda import actualizar, insertar, consultar
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def agregar(roles):
    respuesta = insertar("roles", **roles.__dict__)
    return(respuesta)

def actualiza(filtro, valorFiltro, roles):
    actualizar("roles", filtro, valorFiltro, **roles.__dict__)

def consultas(query):
    return consultar(query)