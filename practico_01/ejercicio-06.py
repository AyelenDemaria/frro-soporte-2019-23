# Implementar la función multiplicar() que devuelva el producto de todos los números de una lista.


# [1,2,3,4] -> 24
def multiplicar(lista):
    valor = 1
    for x in lista:
        valor = valor * x
    return valor

assert (multiplicar([1,2,3,4])) == 24
