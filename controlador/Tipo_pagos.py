from BaseDeDatos.Eda import actualizar, insertar, consultar
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def agregar(tipo_pagos):
    respuesta = insertar("tipo_pagos", **tipo_pagos.__dict__) 
    return(respuesta)

def actualiza(filtro, valorFiltro, tipo_pagos):
    actualizar("tipo_pagos", filtro, valorFiltro, **tipo_pagos.__dict__)

def consultas(query):
    return consultar(query)