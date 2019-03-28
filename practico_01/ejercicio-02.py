# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.


def mayor(a, b, c):
   if a >= b and a >= c:
       return a
   elif b >= a and b >= c:
       return b
   return c

assert mayor(10,9,3) == 10
assert mayor(2,9,3) == 9
assert mayor(2,5,8) == 8
