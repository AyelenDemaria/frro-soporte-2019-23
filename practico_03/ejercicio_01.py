# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import sqlite3 #importo conector
def crear_tabla():
    db = sqlite3.connect('mybase') #creo objeto conexion con connect
    cursor = db.cursor() #creo objeto cursor de la conexion
    cSQL = 'CREATE TABLE IF NOT EXISTS Persona(idPersona INTEGER PRIMARY KEY ASC, nombre TEXT(25), fechaNacimiento DATETIME, dni INTEGER, altura INTEGER )'
    cursor.execute(cSQL) #ejecuto consola con execute del cursor
    db.commit()
    db.close() # cierro

def borrar_tabla():
    connection = sqlite3.connect('mybase')
    cursor = connection.cursor()
    dropTableStatement = "DROP TABLE Persona"
    cursor.execute(dropTableStatement)
    connection.commit()
    connection.close()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
