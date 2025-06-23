from BaseDeDatos.Eda import actualizar, insertar, consultar
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def agregar(contratos):
    respuesta = insertar("contratos", **contratos.__dict__) 
    return(respuesta)

def actualiza(filtro, valorFiltro, contratos):
    actualizar("contratos", filtro, valorFiltro, **contratos.__dict__)

def consultas(query):
    return consultar(query)
    