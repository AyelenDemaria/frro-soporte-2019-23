# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.


from sqlalchemy.orm import sessionmaker
import datetime

from practico_03A.ejercicio_02 import insertarReg
from practico_03A.ejercicio_01 import Persona, engine
from practico_03A.ejercicio_06 import PersonaPeso, reset_tabla

from practico_03A.ejercicio_04 import buscar_persona


Session = sessionmaker(bind = engine)
session = Session()


def agregar_peso(idPersona, fecha, peso):
    res = buscar_persona(idPersona)

    if res != False:
        result = session.query(PersonaPeso).filter(PersonaPeso.idPersona== idPersona, PersonaPeso.fecha > fecha).all()
        if result == []:
               oper = PersonaPeso(idPersona =idPersona, fecha = fecha, peso = peso)
               session.add(oper)
               session.commit()
               resultado = session.query(PersonaPeso).order_by(PersonaPeso.id.desc()).first()
               return resultado.id
        else:
              return False
    else:
        return False



@reset_tabla
def pruebas():
    id_juan = insertarReg('juan perez',datetime.date(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.date(2018, 5, 26), 80) > 0
    #id incorrecto
    assert agregar_peso(200, datetime.date(1988, 5, 15), 80) == False
    #registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.date(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()


