# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine, Date


# ---- datos sqlite en la carpeta actual
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///sqlalchemy_ejercicio1.db')

Base = declarative_base() # Metadatos

class Persona(Base):
    __tablename__ = 'persona' # ----nombre de la tabla
    # Definimos las columnas de la tabla Persona
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(30), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    dni = Column(Integer, nullable=False)
    altura = Column(Integer, nullable=False)



def crear_tabla():
    # Crea todas las tablas definidas en los metadatos
    Base.metadata.create_all(engine)

def borrar_tabla():
    Persona.__table__.drop(engine)


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
