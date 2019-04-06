# Implementar la clase Rectangulo que contiene una base y una altura, y el método area.


class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.alt = altura

    def area(self):
        return self.base*self.alt

x = Rectangulo(2,3)


assert (x.area()) == 6
