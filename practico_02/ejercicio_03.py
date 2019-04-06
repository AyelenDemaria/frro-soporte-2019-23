# Implementar la clase Persona que cumpla las siguientes condiciones:
# Atributos:
# - nombre.
# - edad.
# - sexo (H hombre, M mujer).
# - peso.
# - altura.
# Métodos:
# - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
# - print_data(): imprime por pantalla toda la información del objeto.
# - generar_dni(): genera un número aleatorio de 8 cifras y lo guarda dentro del atributo dni.

from random import randrange
class Persona:

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nom = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.alt = altura
        self.dni = self.generar_dni()

    def es_mayor_edad(self):
        if self.edad >= 21:
            return True
        return False

    # llamarlo desde __init__
    def generar_dni(self):
        return randrange(10000000,99999999)

    def print_data(self):
        return self.nom, self.edad, self.sexo, self.peso, self.alt, self.dni

x = Persona("Ayelen", 21, "Femenino",57,1.6)

assert(x.es_mayor_edad()) == True

