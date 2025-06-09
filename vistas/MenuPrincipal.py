import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controlador.Alumnos import agregar,actualiza
from modelo.Alumnos import Alumnos

alumnos = Alumnos(Nombre = "Pepesssss", Apellido = "otssssro")
agregar(alumnos)
# actualiza("alumnoid", 17, alumnos)
