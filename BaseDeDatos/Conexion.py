# Creado por: Yamil Arribas
# Fecha:
# Descripción: Se utiliza para crear la conexión con la Base de Datos
from dotenv import dotenv_values

def conexionDB():
    config = dotenv_values(".env")
    if config["DRIVER"] == "SQLServer":
        import pyodbc
        connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER="+config["HOST"]+";DATABASE="+config["DB"]+";Trusted_Connection=yes;"
        conn = pyodbc.connect(connection_string)
        return conn
    elif config["DRIVER"]== "MySQL":
        import mysql.connector
        connection_data = {
            "user": config["USER"],
            "password": config["PASSWORD"],
            "host": config["HOST"],
            "database": config["DB"]
        }
        try:
            conn = mysql.connector.connect(**connection_data)
            if conn.is_connected():
                print("Conexión exitosa")
                return conn
        except mysql.connector.Error as err:
            print(f"Error: {err}")