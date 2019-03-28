# Implementar la función es_palindromo(), que devuelva un booleano en base a
# si palabra se lee igual de corrido como al revés.


# Ejemplos: arenera, radar, ojo, oso, salas.
# Resolver sin utilizar loops (for/while), sino con slicing.
def es_palindromo(palabra):
    rever = palabra[::-1]
    if palabra == rever:
       return True
    return False

assert (es_palindromo('eliana')) == False
assert (es_palindromo('arenera')) == True

