# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.


from sqlalchemy.orm import sessionmaker
import datetime

from practico_03A.ejercicio_01 import reset_tabla, Persona, engine

Session = sessionmaker(bind = engine)
session = Session()

def insertarReg(nombre, fecha, dni, altura):
    oper = Persona(nombre = nombre,fecha_nacimiento = fecha, dni = dni, altura = altura)
    session.add(oper)
    session.commit()
    result = session.query(Persona).order_by(Persona.id.desc()).first()
    return result.id


@reset_tabla
def pruebas():
    id_juan = insertarReg('juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    id_marcela = insertarReg('marcela gonzalez', datetime.date(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()

