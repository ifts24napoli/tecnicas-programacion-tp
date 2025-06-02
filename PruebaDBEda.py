# Este es un modulo para ralizar Pruebas de AMB en la base de datos

from BaseDeDatos.Eda import eleiminar, actualizar, insertar, consultar
 
    
def main():
     #Ejemolos filtro Texto eleiminar("alumnos", "apellido", "'Lusto'")
     #Ejemplo filtro entero eleiminar("alumnos","apellido", 54)
    # eleiminar("alumnos", "alumnoId", 66)
    # actualizar("alumnos", "alumnoID", "64" , Nombre = "Martin", Apellido = "Lista", Edad = 44, Grado = "Secundario")
    insertar("alumnos", Apellido = 'Alarcon', Nombre = 'Roxana',  Edad = 39, Grado = "Primero")
    # consultar("Select * from alumnos where nombre = 'Yamil'")
       
if __name__ == "__main__":  # Evita que el código se ejecute automáticamente si el archivo es importado como módulo
    main()            