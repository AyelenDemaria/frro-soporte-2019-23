# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.


from sqlalchemy import Column, ForeignKey, Integer,Date
from sqlalchemy.orm import relationship

from practico_03A.ejercicio_01 import Persona, engine, Base, borrar_tabla, crear_tabla



class PersonaPeso(Base):
    __tablename__ = 'personaPeso' # ----nombre de la tabla
    # Definimos las columnas de la tabla Persona
    id = Column(Integer, primary_key=True, autoincrement=True)
    idPersona = Column(Integer, ForeignKey(Persona.id))
    fecha = Column(Date, nullable=False)
    peso = Column(Integer, nullable=False)


def crear_tabla_peso():
    Base.metadata.create_all(engine)

def borrar_tabla_peso():
    PersonaPeso.__table__.drop(engine)



# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
