# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).

from datetime import datetime
class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):
        self.nac = nacimiento

    def edad(self):
        fechanac = datetime.strptime(self.nac,"%Y-%m-%d")
        anionac = fechanac.year
        mesnac = fechanac.month
        dianac = fechanac.day
        if mesnac < datetime.now().month:
            return datetime.now().year - anionac
        elif mesnac > datetime.now().month:
            return (datetime.now().year - anionac) - 1
        elif dianac < datetime.now().day:
           return datetime.now().year - anionac
        return (datetime.now().year - anionac) - 1


x = Persona("1991-08-28")
assert (x.edad()) == 27



