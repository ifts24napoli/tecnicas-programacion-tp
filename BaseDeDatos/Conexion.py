# Creado por: Yamil Arribas
# Fecha:
# Descripción: Se utiliza para crear la conexión con la Base de Datos
import os
from dotenv import load_dotenv

def conexionDB():
    load_dotenv()
    host = os.getenv('HOST')
    db = os.getenv('DB')
    driver = os.getenv('DRIVER')
    print(driver)
    if driver == "SQLServer":
        import pyodbc
        connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER="+host+";DATABASE="+db+";Trusted_Connection=yes;"
        conn = pyodbc.connect(connection_string)
        return conn
    elif driver == "MySQL":
        import mysql.connector
        host = os.getenv("HOST")
        user = os.getenv("USER")
        password = os.getenv("PASSWORD")
        connection_data = {
            "user": user,
            "password": password,
            "host": host,
            "database": db
        }
        try:
            conn = mysql.connector.connect(**connection_data)
            if conn.is_connected():
                print("Conexión exitosa")
                return conn
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    elif driver == "SQLite":
        import sqlite3
        conn = sqlite3.connect(db + ".db")
        return conn
    else:
        print("Error: motor inválido")