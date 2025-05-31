from BaseDeDatos.DBManager import DBManager

db = DBManager()
def consultar(query): 
    consulta = db.consultar(query)
    if "Error" in consulta:
        print(consulta)
    else:    
        for item in consulta:
            print(item)

def insertar(tabla,**datos):
    valores = []
    columnas = []
    for clave, valor in datos.items():
        columnas.append(clave)
        if isinstance (valor,str):
            valores.append(f"'{valor}'")
        else:
            valores.append(str(valor))   
    valores_sql = ", ".join(valores) 
    columnas_sql = ", ".join(columnas)           
    respuesta = db.agregar(f"insert into {tabla} ({columnas_sql}) values ({valores_sql})")
    print(respuesta)

def actualizar(nbrTabla,filtro,valorFiltro,**datos):
    valores = []
    for clave, valor in datos.items():
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
    

def eleiminar(tabla,filtro, valorFiltro):
    respuesta = db.eliminar(f"Delete from {tabla} where {filtro} = {valorFiltro}")
    print(respuesta) 