from BaseDeDatos.Eda import actualizar, insertar, consultar
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def agregar(clientes):
    respuesta = insertar("clientes", **clientes.__dict__)
    return(respuesta)

def actualiza(filtro, valorFiltro, clientes):
    actualizar("clientes", filtro, valorFiltro, **clientes.__dict__)

def consultas(query):
    return consultar(query)