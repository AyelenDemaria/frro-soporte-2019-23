# Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
# - id_socio: entero (clave primaria, auto-incremental, unico)
# - dni: entero (unico)
# - nombre: string (longitud 250)
# - apellido: string (longitud 250)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from sqlalchemy import create_engine
Base = declarative_base()
engine = create_engine('sqlite:///sqlalchemy_ejercicio1-5.db')



class Socio(Base):
    __tablename__ = 'socios'
    id_socio = Column(Integer, primary_key=True, autoincrement=True)
    dni = Column(Integer, nullable=False)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)

def crear_tabla():
    # Crea todas las tablas definidas en los metadatos
    Base.metadata.create_all(engine)


crear_tabla()
