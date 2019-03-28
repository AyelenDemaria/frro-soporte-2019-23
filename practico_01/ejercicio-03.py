# Implementar la función operacion, donde:
# - Si multiplicar es True: devolver la multiplicación entre a y b.
# - Si multiplicar es False: devolver la division entre a y b.
# - Si multiplicar es False y b es cero: imprimir por consola "Operación no valida".


def operacion(a, b, multiplicar):
  if multiplicar == True:
      return (a * b)
  elif b == 0:
    return "Operación no valida"
  return a / b

assert operacion(10, 2, True) == 20
assert operacion(10, 2, False) == 5.0
assert operacion(10, 0, False) == "Operación no valida"

