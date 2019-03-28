# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


# se debe implementar utilizando bucles anidados.
def superposicion_loop(lista_1, lista_2):
    b = 'F'
    for i in lista_1:
        for j in lista_2:
           if i == j:
               b = 'T'
               break

    if b == 'T':
       return True
    return False

assert(superposicion_loop(['n',9,0],[1,5,'n'])) == True
assert(superposicion_loop(['n',9,0],[1,5,7])) == False



# se debe implementar utilizando conjuntos (sets).
def superposicion_set(lista_1, lista_2):
     if (set(lista_1) & set(lista_2)) != set(): #set() es un conjunto vacio
         return True
     return False

assert(superposicion_set(['n',9,0],[1,5,'n'])) == True
assert(superposicion_set(['n',9,0],[1,5,7])) == False
