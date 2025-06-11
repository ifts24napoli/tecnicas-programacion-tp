# Creado por: Yamil Arribas
# Fecha:
# Descripción: Clase para realizar operaciones de AMB en una Base de Datos

import pyodbc, os
from BaseDeDatos.Conexion import conexionDB

class DBManager:
    # Constructor: inicializa los atributos del objeto al momento de su creación (instanciación)
    def __init__(self):
        self.conn = conexionDB()
        self.cursor = self.conn.cursor()
        nombre_script = os.getenv('INICIALIZACION')
        if nombre_script:
            archivo_script = open(nombre_script, 'r')
            contenido_script = archivo_script.read()
            archivo_script.close()
            self.scursor = self.cursor.executescript(contenido_script)
            self.conn.commit()

    def consultar(self, query: str,):
        try:
            self.cursor.execute(query)
            resultado = self.cursor.fetchall()
            return resultado
        except pyodbc.Error as e:
            return f"Error al consultar: {e}"
        
    def agregar(self, query: str):
        try:
            query = query + " ;SELECT SCOPE_IDENTITY();" # Necesario para devolver el valor del id creado
            self.cursor.execute(query) # Ejecuta la consulta en la BD
            self.cursor.nextset()  #Me muevo al siguiente resultado (el SELECT)
            id_nuevo = self.cursor.fetchone()[0] #Obtengo el id del nuevo registro
            self.conn.commit()  # Asegura que se guarde en la BD
            return ([int(id_nuevo), "El resgistro se agrego Correctamente"])
        except pyodbc.Error as e:
            return f"Error al insertar datos: {e}"
    
    def actualizar(self, query: str):
        try:
            filas = self.cursor.execute(query).rowcount
            self.conn.commit()
            if filas <= 0:
                return("No se encontro el registro")
            else:
                return ("Los registros se actualizaron Correctamente")
        except pyodbc.Error as e:
            return f"Error en la actualizacion: {e}"
    
    def eliminar(self, query: str):
        try:
            self.cursor.execute(query)
            self.conn.commit()
            if self.cursor.rowcount == 0:
                return "No hay registros para eliminar"
            return f"Se eliminaron {self.cursor.rowcount} registro/s Correctamente"
        except pyodbc.Error as e:
            return f"Error en la eliminacion: {e}"
            
                             
  
