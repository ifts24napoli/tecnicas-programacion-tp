import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from vistas.ABMUsuario import abm

while True:
    print(""" Selecciones una de las siguientes opciones: \n 
          0 Para Salir \n
          1 Gestion de Ususario \n
          """)
    opcion = int(input("Ingrese Alguna Opcion: "))
    if opcion == 0:
        break
    elif opcion == 1:
        abm()
