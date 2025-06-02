from BaseDeDatos.DBManager import DBManager

db = DBManager()
consulta = db.consultar('Select * from alumnos')
if "Error" in consulta:
    print(consulta)
else:    
    for item in consulta:
        print(item)

actualizacion = db.agregar("insert into alumnos (nombre, apellido)  values ('Yami', 'Arribas')")    
print(actualizacion)  

  

