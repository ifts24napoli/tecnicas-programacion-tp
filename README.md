# TP de Técnicas de Programación (IFTS Nº24)
Sistema para Gestión interna de una empresa ISP (proveedor de servicio de internet)

## Instalación
- ejecutar script para crear BD y tablas (sqlserver/mysql/sqlite3)
- crear archivo .env en el directorio raíz con la siguiente configuración:
    ```
        DRIVER="SQLServer|MySQL|SQLite"
        HOST="localhost"
        DB="DBTP"
    ```
- instalar bibliotecas (ver requerimientos)

## Requerimientos
- dotenv (`pip install dotenv`)
- conexión con DB: SQLServer (`pip install pyocdb`), MySQL (`pip install mysql.connector`) o sqlite3 (`pip install sqlite3`)

## Uso
- ejecutar Ingreso.py
- autenticarse con e-mail y contraseña