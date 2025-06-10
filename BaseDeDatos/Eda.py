# Creado por: Yamil Arribas
# Fecha: [completar fecha si querés]
# Descripción: 
# EDA = Easy Data Access. Módulo diseñado para facilitar tareas de ABM (Alta, Baja, Modificación) 
# en una base de datos sin necesidad de escribir sentencias SQL directamente.
# Su objetivo es permitir la reutilización y ejecución sencilla de acciones sobre una base de datos,
# brindando una interfaz simple y amigable para el usuario.

from BaseDeDatos.DBManager import DBManager

db = DBManager() # Creo el objeto db para trabajar con la base de datos

def consultar(query): 
    consulta = db.consultar(query)
    if "Error" in consulta:
        print(consulta)
    else:    
        for item in consulta:
            print(item)
        return consulta
def insertar(tabla,**datos): # Utilizamos parametros de tipo keyword arguments (Clave - Valor) como los Dic.
    valores = []
    columnas = []
    for clave, valor in datos.items():
        if valor is not None:
            columnas.append(clave)
            if isinstance (valor,str):
                valores.append(f"'{valor}'")
            else:
                valores.append(str(valor))   
    valores_sql = ", ".join(valores) 
    columnas_sql = ", ".join(columnas)           
    respuesta = db.agregar(f"insert into {tabla} ({columnas_sql}) values ({valores_sql})")
    return respuesta

def actualizar(nbrTabla,filtro,valorFiltro,**datos): # Utilizamos parametros de tipo keyword arguments (Clave - Valor) como los Dic.
    valores = []
    for clave, valor in datos.items():
        if valor is not None:
            if isinstance(valor,str):
                valores.append(f"{clave} = '{valor}'")
            else:
                valores.append(f"{clave} = {str(valor)}")  
    valores_sql = ", ".join(valores)  
    if not valorFiltro :
        print("Error: debe incluir el ID para actualizar el registro.")
        return      
    respuesta = db.actualizar(f"""update {nbrTabla} set {valores_sql} where {filtro} = {valorFiltro};""")     
    print(respuesta)
    

def eleiminar(tabla, filtro, valorFiltro):
    if isinstance(valorFiltro, str):
        valorFiltro = f"'{valorFiltro}'"
    respuesta = db.eliminar(f"Delete from {tabla} where {filtro} = {valorFiltro}")
    print(respuesta) 
    