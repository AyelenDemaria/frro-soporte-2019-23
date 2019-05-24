#Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.


from sqlalchemy.orm import sessionmaker
import datetime

from practico_03A.ejercicio_01 import reset_tabla, Persona, engine
from practico_03A.ejercicio_02 import insertarReg

Session = sessionmaker(bind = engine)
session = Session()
session = Session()

def borrar_persona(idPersona):
    sq = session.query(Persona).filter(Persona.id == idPersona).first()
    if sq != None:
        session.delete(sq)
        session.commit()
        return True
    else:
        return False


@reset_tabla
def pruebas():

    assert borrar_persona(insertarReg('juan perez', datetime.date(1988, 5, 15), 32165498, 180)) is True
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
