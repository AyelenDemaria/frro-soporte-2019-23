# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).

import practico_02.ejercicio_03 as m
from datetime import datetime
class Estudiante(m.Persona):

    def __init__(self, nombre, edad, sexo, peso, altura, carrera, anio, cantidad_materias, cantidad_aprobadas):
        m.Persona.__init__(self, nombre, edad, sexo, peso, altura)
        self.car = carrera
        self.anio = anio
        self.cant = cantidad_materias
        self.cantAp = cantidad_aprobadas

    def avance(self):
        return round((self.cantAp * 100) / self.cant, 2)

    # implementar usando modulo datetime
    def edad_ingreso(self):
        year = datetime.now().year
        return self.edad - (year - self.anio)

x = Estudiante("Ayelen", 21, "Femenino",57,1.6, "ISI", 2016, 41,23)
assert(x.avance()) == 56.1
assert(x.edad_ingreso()) == 18
