# Este módulo permite realizar operaciones ABM sobre comodatos, verificando y ajustando stock.
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importación de funciones del controlador y modelo
from controlador.Planes import agregar, actualiza, consultas
from modelo.Planes import Planes

# Función principal del menú Planes
def abmPlanes():
    while True:
        print("""
        ==========================
        |        Planes          |
        ==========================
        | 0. Salir               |
        | 1. Crear Plan          |
        | 2. Modificar Plan      |
        | 3. Listar Planes       |
        ==========================
        """)
        try:
            # Se solicita la opción y se convierte a entero
            opcion = int(input("Ingrese una opción: "))
            if opcion == 0:
                break
            elif opcion == 1:
                crearPlan()
            elif opcion == 2:
                modificarPlan()
            elif opcion == 3:
                listarPlanes()
            else:
                print("Opción inválida.")
        except ValueError:
            # Captura errores si se ingresa algo que no sea número
            print("Debe ingresar un número válido.")
            continue


# Crea un nuevo plan solicitando descripción y precio
# Verifica con el usuario si desea guardar
def crearPlan():
    print("=== Crear Nuevo Plan ===")
    plan = Planes()

    try:
        plan.descripcion = input("Ingrese la descripción del plan: ").strip()
        if not plan.descripcion:
            raise ValueError("La descripción no puede estar vacía.")

        while True:
            precio_input = input("Ingrese el precio del plan: ").strip()
            try:
                precio = float(precio_input)
                if precio <= 0:
                    print("El precio debe ser un número mayor que cero.")
                    continue
                plan.precio = precio
                break
            except ValueError:
                print("Debe ingresar un número válido.")

        confirmacion = input("¿Desea guardar este plan? (s/n): ")
        if confirmacion.lower() == "s":
            respuesta = agregar(plan)
            print(respuesta[1])
        else:
            print("No se guardó el plan.")

    except ValueError as ve:
        print(f"Error: {ve}")



# Permite modificar un plan existente
# Muestra la lista de planes y solicita el ID a modificar
# Los campos se pueden dejar en blanco para conservar el valor anterior
def modificarPlan():
    while True:
        try:
            print("=== Modificar Plan ===")
            resultado = listarPlanes()
            id_plan = int(input("Ingrese el ID del plan a modificar: "))
            validarPlan = consultas(f"""SELECT id_planes, descripcion, precio FROM planes
                                        WHERE id_planes = '{id_plan}'""")
            if not validarPlan:
                print("El ID del plan no existe.")
                continue
            break
        except ValueError:
            print("Debe ingresar un valor numérico.")

    descripcion = input("Nueva descripción (opcional, dejar en blanco si no quiere cambiarla): ")
    
    # Validación del nuevo precio
    while True:
        precio_input = input("Nuevo precio (opcional, dejar en blanco si no quiere cambiarlo): ").strip()
        if precio_input == "":
            precio = resultado[0][2]  # Mantener precio actual
            break
        try:
            precio = float(precio_input)
            if precio <= 0:
                print("El precio debe ser un número mayor a cero.")
                continue
            break
        except ValueError:
            print("Ingrese un número válido para el precio.")

    # Armado del objeto plan
    plan = Planes()
    plan.descripcion = descripcion if descripcion else resultado[0][1]
    plan.precio = precio

    confirmacion = input("¿Confirma los cambios? (s/n): ")
    if confirmacion.lower() == "s":
        actualiza("id_planes", id_plan, plan)
        print("Plan actualizado correctamente.")
    else:
        print("No se realizaron cambios.")


# Lista todos los planes existentes mostrando su ID, descripción y precio
# Devuelve la lista para poder ser reutilizada por otras funciones
def listarPlanes():
    print("=== Lista de Planes ===")
    resultados=consultas("SELECT id_planes, descripcion, precio FROM planes")
    
    if not resultados:
        print("No se encontraron planes.")
        return
    
    for fila in resultados:
        id_plan, descripcion, costo = fila
        print(f"ID: {id_plan}, Descripción: {descripcion}, Precio: ${float(costo):.2f}")
    
    return resultados


#abmPlanes()

