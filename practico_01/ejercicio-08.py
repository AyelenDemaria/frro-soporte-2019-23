# Implementar la función mitad(), que devuelve la mitad de palabra.
# Si la longitud es impar, redondear hacia arriba.


# hola -> ho
# verde -> ver
def mitad(palabra):

   tam = len(palabra)
   mit = int(tam / 2)
   if not ((tam % 2) == 0):
       return palabra[0:mit+1]
   return palabra[0:mit]

assert mitad('hola') == 'ho'
assert mitad('verde') == 'ver'


