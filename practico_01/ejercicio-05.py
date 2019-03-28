# Implementar la función es_vocal, que reciba un carácter y
# devuelva un booleano en base a si letra es una vocal o no.


# Resolver utilizando listas y el operador in.
def es_vocal(letra):
  if letra in ['a','e','i','o','u']:
      return True
  return False

assert (es_vocal('a')) == True
assert (es_vocal('b')) == False
