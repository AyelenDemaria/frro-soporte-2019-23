# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.

import math
class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return round(math.pi * (self.radio**2), 2)

    def perimetro(self):
        return 2 * self.radio

x = Circulo (3)
assert(x.area()) == 28.27
assert(x.perimetro()) == 6
