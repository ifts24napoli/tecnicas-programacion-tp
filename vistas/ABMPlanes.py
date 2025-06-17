import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controlador.Planes import agregar, actualiza, consultas
from modelo.Planes import Planes

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
            print("Debe ingresar un número válido.")
            continue


def crearPlan():
    print("=== Crear Nuevo Plan ===")
    plan = Planes()
    plan.descripcion = input("Ingrese la descripción del plan: ")
    plan.precio = float(input("Ingrese el precio del plan: "))
    
    confirmacion = input("¿Desea guardar este plan? (s/n): ")
    if confirmacion.lower() == "s":
        respuesta = agregar(plan)
        print(respuesta[1])
    else:
        print("No se guardó el plan.")


def modificarPlan():
    print("=== Modificar Plan ===")
    resultado = listarPlanes()
    id_plan = int(input("Ingrese el ID del plan a modificar: "))
    
    descripcion = input("Nueva descripción (opcional, dejar en blanco si no quiere cambiarlo): ")
    precio = input("Nuevo precio (opcional, dejar en blanco si no quiere cambiarlo): ")
    
    plan = Planes()
    
    if descripcion:
        plan.descripcion = descripcion
    if precio:
        plan.precio = float(precio)
    else:
        plan.precio= resultado[0][2]

    confirmacion = input("¿Confirma los cambios? (s/n): ")
    if confirmacion.lower() == "s":
        actualiza("id_planes", id_plan, plan)
        print("Plan actualizado correctamente.")
    else:
        print("No se realizaron cambios.")


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



