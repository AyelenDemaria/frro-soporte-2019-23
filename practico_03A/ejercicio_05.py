# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

from sqlalchemy.orm import sessionmaker
import datetime

from practico_03A.ejercicio_01 import reset_tabla, Persona, engine
from practico_03A.ejercicio_02 import insertarReg
from practico_03A.ejercicio_04 import buscar_persona

Session = sessionmaker(bind = engine)
session = Session()
session = Session()

def actualizar_persona(idPersona, nom, fecha, dni, alt):
     res = buscar_persona(idPersona)
     if res != False:
         sq = session.query(Persona).filter(Persona.id == idPersona).first()
         sq.nombre = nom
         sq.fecha_nacimiento = fecha
         sq.dni = dni
         sq.altura = alt
         session.commit()
         return True
     else:
         return False

@reset_tabla
def pruebas():
    id_juan = insertarReg('juan perez', datetime.date(1988, 5, 15), 32165498, 180)

    assert actualizar_persona(id_juan, 'juan carlos perez', datetime.date(1988, 4, 16), 32165497, 181) is True
    assert actualizar_persona(123, 'nadie', datetime.date(1988,4,16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()


