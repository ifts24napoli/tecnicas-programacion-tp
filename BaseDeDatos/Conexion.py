# Creado por: Yamil Arribas
# Fecha:
# Descripción: Se utiliza para crear la conexión con la Base de Datos
import pyodbc

def conexionDB():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-EEGJP86;'
        'DATABASE=dbtp;'
        'Trusted_Connection=yes;'
    )
    return conn
