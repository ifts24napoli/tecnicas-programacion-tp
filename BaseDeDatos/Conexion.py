import pyodbc

def conexionDB():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-EEGJP86;'
        'DATABASE=dbescuela;'
        'Trusted_Connection=yes;'
    )
    return conn
