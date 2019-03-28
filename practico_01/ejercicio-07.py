# Implementar la función numeros_al_final(), que mueve todos los elementos numéricos
# de lista al final de esta. Devuelve la lista.


# Resolver sin utilizar lista auxiliar

def numeros_al_final(lista):
    tam = len(lista)
    cont = 0
    i = 0
    while cont in range(tam):
            if type(lista[i]) != str:
                lista.append(lista[i])
                lista.remove(lista[i])
            else: i += 1
            cont += 1
    return lista

assert(numeros_al_final(['o','y',0,9,6,3,'p',5,'l'])) == ['o', 'y', 'p', 'l', 0, 9, 6, 3, 5]




