# Este módulo permite realizar operaciones ABM sobre comodatos, verificando y ajustando stock.
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importación de funciones del controlador y modelo
from controlador.Comodato import consultas as consulta_comodato, agregar as agregar_comodato, actualiza, eleiminar as eliminar_comodato
from controlador.Inventario import consultas as consulta_inventario, actualizar_stock
from modelo.Comodato import Comodato

# Función para validar que la entrada del usuario sea un número válido antes de continuar
def input_numerico(mensaje, entero=True):
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return int(valor) if entero else float(valor)
        print("Entrada no válida. Ingrese un número.")

# Función principal del menú Comodato
def abmComodato():
    while True:
        print("""
        =============================
        |       ABM Comodato        |
        =============================
        | 0. Salir                  |
        | 1. Listar Comodatos       |
        | 2. Generar Comodato       |
        | 3. Modificar Comodato     |
        | 4. Eliminar Comodato      |
        =============================
        """)
        opcion = input("Seleccione una opción: ")

        
        if opcion == "0":
            break
        elif opcion == "1":
            listar_comodatos()
        elif opcion == "2":
            generar_comodato()
        elif opcion == "3":
            modificar_comodato()
        elif opcion == "4":
            eliminar_comodato_vista()
        else:
            print("Opción no válida.")

# Función que lista todos los comodatos registrados en la base de datos
# Realiza una consulta simple y recorre el resultado para mostrar los registros

def listar_comodatos():
    print("\n--- Lista de Comodatos ---")
    query = "SELECT * FROM comodato"
    resultado = consulta_comodato(query)

    if resultado:
        for fila in resultado:
            print(f"ID: {fila[0]} | Cantidad: {fila[1]} | ID Inventario: {fila[2]} | ID Contrato: {fila[3]}")
    else:
        print("No hay comodatos registrados.")

# Función que permite generar un nuevo comodato
# Verifica que exista el inventario, que haya suficiente stock y actualiza la base

def generar_comodato():
    # Solicita ID del inventario y cantidad a prestar, con validación
    id_inventario = input_numerico("Ingrese ID del inventario: ")
    cantidad = input_numerico("Ingrese cantidad a prestar en comodato: ")

    # Consulta si el inventario existe
    query = f"SELECT * FROM inventario WHERE id_inventario = {id_inventario}"
    resultado = consulta_inventario(query)

    if not resultado:
        print("Inventario no encontrado.")
        return

    stock_disponible = resultado[0][1]

    # Verifica si la cantidad solicitada es mayor al stock disponible
    if cantidad > stock_disponible:
        print(f"No hay suficiente stock. Disponible: {stock_disponible}")
        return

    # Mostramos contratos disponibles antes de solicitar el ID
    print("\n--- Contratos disponibles ---")
    contratos = consulta_comodato("SELECT * FROM contrato")  

    if contratos:
        for contrato in contratos:
            print(f"ID: {contrato[0]} | Fecha alta: {contrato[1]} | Id cliente: {contrato[4]}")  
    else:
        print("No hay contratos registrados.")
        return  # salimos si no hay contratos

    # Solicita el ID del contrato asociado al comodato
    id_contrato = input_numerico("Ingrese ID del contrato asociado: ")

    # Crea objeto Comodato y lo inserta en la base de datos
    datos = {
        "Id_comodato": None,
        "Cantidad": cantidad,
        "Id_inventario": id_inventario,
        "Id_contrato": id_contrato
    }
    nuevo_comodato = Comodato(**datos)
    agregar_comodato(nuevo_comodato)

    # Actualiza el stock en inventario restando la cantidad prestada
    nuevo_stock = stock_disponible - cantidad
    actualizar_stock(id_inventario, nuevo_stock)

    print("Comodato creado exitosamente.")

# Función para modificar un comodato existente
# Permite modificar cantidad, inventario o contrato, y actualiza stock si cambió

def modificar_comodato():
    id_comodato = input_numerico("Ingrese el ID del comodato a modificar: ")

    query = f"SELECT * FROM comodato WHERE id_comodato = {id_comodato}"
    resultado = consulta_comodato(query)

    if not resultado:
        print("Comodato no encontrado.")
        return

    # Obtiene valores actuales del comodato
    registro_actual = resultado[0]
    cantidad_anterior = registro_actual[1]
    id_inventario_anterior = registro_actual[2]
    id_contrato_anterior = registro_actual[3]

    print("Ingrese los nuevos datos (dejar en blanco para mantener):")
    cantidad_input = input(f"Cantidad [{cantidad_anterior}]: ")
    id_inventario_input = input(f"ID Inventario [{id_inventario_anterior}]: ")
    id_contrato_input = input(f"ID Contrato [{id_contrato_anterior}]: ")

    # Se mantienen los datos actuales si el usuario no ingresa nuevos valores
    nueva_cantidad = int(cantidad_input) if cantidad_input.isdigit() else cantidad_anterior
    nuevo_id_inventario = int(id_inventario_input) if id_inventario_input.isdigit() else id_inventario_anterior
    nuevo_id_contrato = int(id_contrato_input) if id_contrato_input.isdigit() else id_contrato_anterior

    # Si cambia cantidad o inventario, se ajusta el stock respectivo
    if nueva_cantidad != cantidad_anterior or nuevo_id_inventario != id_inventario_anterior:
        # Restaura el stock anterior
        inventario_ant = consulta_inventario(f"SELECT * FROM inventario WHERE id_inventario = {id_inventario_anterior}")
        if inventario_ant:
            stock_ant = inventario_ant[0][1]
            actualizar_stock(id_inventario_anterior, stock_ant + cantidad_anterior)

        # Verifica existencia y stock en nuevo inventario
        inventario_nuevo = consulta_inventario(f"SELECT * FROM inventario WHERE id_inventario = {nuevo_id_inventario}")
        if not inventario_nuevo:
            print("Nuevo inventario no encontrado.")
            return

        stock_nuevo = inventario_nuevo[0][1]
        if nueva_cantidad > stock_nuevo:
            print(f"No hay suficiente stock en el nuevo inventario. Disponible: {stock_nuevo}")
            return

        # Actualiza stock en nuevo inventario
        actualizar_stock(nuevo_id_inventario, stock_nuevo - nueva_cantidad)

    # Prepara objeto actualizado y lo guarda
    datos_modificados = {
        "Id_comodato": id_comodato,
        "Cantidad": nueva_cantidad,
        "Id_inventario": nuevo_id_inventario,
        "Id_contrato": nuevo_id_contrato
    }

    comodato_modificado = Comodato(**datos_modificados)
    actualiza("id_comodato", id_comodato, comodato_modificado)

    print("Comodato modificado y stock actualizado.")

# Función que permite eliminar un comodato existente
# Restaura automáticamente el stock del inventario asociado

def eliminar_comodato_vista():
    id_comodato = input_numerico("Ingrese el ID del comodato a eliminar: ")

    query = f"SELECT * FROM comodato WHERE id_comodato = {id_comodato}"
    resultado = consulta_comodato(query)

    if not resultado:
        print("Comodato no encontrado.")
        return

    # Recupera cantidad e inventario para restaurar stock
    cantidad = resultado[0][1]
    id_inventario = resultado[0][2]

    confirmacion = input("¿Está seguro que desea eliminar este comodato? (s/n): ").lower()
    if confirmacion == "s":
        # Restaura stock al inventario original
        inventario_resultado = consulta_inventario(f"SELECT * FROM inventario WHERE id_inventario = {id_inventario}")
        if inventario_resultado:
            stock_actual = inventario_resultado[0][1]
            nuevo_stock = stock_actual + cantidad
            actualizar_stock(id_inventario, nuevo_stock)

        # Elimina el comodato del sistema
        eliminar_comodato("id_comodato", id_comodato)
        print("Comodato eliminado y stock restaurado correctamente.")
    else:
        print("Eliminación cancelada.")


"""if __name__ == "__main__":
    abmComodato()"""