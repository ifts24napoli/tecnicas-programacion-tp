# Este es un modulo para ralizar Pruebas de AMB en la base de datos
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BaseDeDatos.Eda import eleiminar, actualizar, insertar, consultar
 
def agregar(alumnos):
  insertar("alumnos", **alumnos.__dict__) #**alumnos.__dict__ convierto el objeto a Diccionario
# actualizar("alumnos", "alumnoid", '10', **alumnos.__dict__)
  #Ejemolos filtro Texto eleiminar("alumnos", "apellido", "'Lusto'")
  #Ejemplo filtro entero eleiminar("alumnos","apellido", 54) 
# eleiminar("alumnos", "alumnoid", 79) 
# consultar("Select * from alumnos where nombre = 'Yamil'")         
 
def actualiza(filtro, valorFiltro, alumnos):
  actualizar("alumnos", filtro, valorFiltro, **alumnos.__dict__)