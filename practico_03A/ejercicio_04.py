# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

from sqlalchemy.orm import sessionmaker
import datetime

from practico_03A.ejercicio_01 import reset_tabla, Persona, engine
from practico_03A.ejercicio_02 import insertarReg

Session = sessionmaker(bind = engine)
session = Session()
session = Session()


def buscar_persona(idPersona):

    sq = session.query(Persona).filter(Persona.id == idPersona).first()
    if sq != None:
        return sq.id, sq.nombre,sq.fecha_nacimiento, sq.dni, sq.altura
    else:
        return False



@reset_tabla
def pruebas():
    juan = buscar_persona(insertarReg('juan perez', datetime.date(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
