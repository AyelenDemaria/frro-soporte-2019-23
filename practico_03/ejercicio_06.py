# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from practico_03.ejercicio_01 import borrar_tabla, crear_tabla

import sqlite3
def crear_tabla_peso():
    db = sqlite3.connect('mybase')
    cursor = db.cursor()
    cSQL = 'CREATE TABLE IF NOT EXISTS PersonaPeso(idPersona INTEGER, fecha DATE, peso INTEGER, FOREIGN KEY (idPersona) REFERENCES Persona(idPersona))'
    cursor.execute(cSQL)
    cursor.close()
    db.commit()
    db.close()


def borrar_tabla_peso():
    connection = sqlite3.connect('mybase')
    cursor = connection.cursor()
    dropTableStatement = "DROP TABLE PersonaPeso"
    cursor.execute(dropTableStatement)
    connection.commit()
    connection.close()



# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
