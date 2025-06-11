import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from vistas.ABMUsuario import abmUsuarios
from vistas.ABMClientes import abmClientes

def main():
    while True:
        print(""" Selecciones una de las siguientes opciones:
            0 Para Salir
            1 Gestion de Ususario
            2 Gestion de Clientes 
            """)
        try: 
            opcion = int(input("Ingrese Alguna Opcion: "))
            if opcion == 0:
                break
            elif opcion == 1:
                abmUsuarios()
            elif opcion	 == 2:
                abmClientes()     
        except ValueError:
            print("Debe ingresar un valor numérico")        
if __name__ == "__main__":
    main()