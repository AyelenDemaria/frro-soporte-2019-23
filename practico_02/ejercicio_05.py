# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from practico_02.ejercicio_04 import Estudiante

# Suponemos las carreras de la facultad ISI, IE, IQ, IC, IM
def organizar_estudiantes(estudiantes):
    dic = {"ISI":0, "IC":0, "IE":0, "IM":0, "IQ":0}
    for i in estudiantes:
        if i.car in dic:
            dic[i.car] += 1
    return dic


x = Estudiante("Ayelen", 21, "Femenino",57,1.6, "ISI", 2016, 41,23)
y = Estudiante("Eliana", 26, "Femenino", 56, 1.7,"IC", 2011,40, 23)
z = Estudiante("Paulino", 23, "Masculino", 75, 1.8, "ISI", 2015, 41, 19)
c = Estudiante("Andres", 24, "Masculino", 70, 1.65, "IE", 2013, 38, 16)

assert(organizar_estudiantes([x,y,z,c])) == {'ISI': 2, 'IC': 1, 'IE': 1, 'IM': 0, 'IQ': 0}

