# Creado por: Yamil Arribas
# Fecha:
# Descripción: Clase para realizar operaciones de AMB en una Base de Datos

import pyodbc
from BaseDeDatos.Conexion import conexionDB

class DBManager:
    # Constructor: inicializa los atributos del objeto al momento de su creación (instanciación)
    def __init__(self):
        self.conn = conexionDB()
        self.cursor = self.conn.cursor()

    def consultar(self, query: str,):
        try:
            self.cursor.execute(query)
            resultado = self.cursor.fetchall()
            return resultado
        except pyodbc.Error as e:
            return f"Error al consultar: {e}"
        
    def agregar(self, query: str):
        try:
            self.cursor.execute(query) # Ejecuta la consulta en la BD
            self.conn.commit()  # Asegura que se guarde en la BD
            return ("Los registros se insertaron Correctamente")
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
            
                             
  
