# Implementar los casos de prueba descriptos.

import unittest

from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio,DniRepetido,LongitudInvalida,MaximoAlcanzado


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.negS = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.negS.datos.borrar_todos()

    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.negS.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12312312, nombre='Juan', apellido='Perez')
        exito = self.negS.alta(socio)

       # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.negS.todos()), 1)

    def test_regla_1(self):
        valido = Socio(dni=45645645, nombre="Jose", apellido="Fernandez")
        self.assertTrue(self.negS.regla_1(valido))

        # DNI socio repetido
        invalido = Socio(dni=12312312, nombre="Juan", apellido="Perez")
        self.assertRaises(DniRepetido, self.negS.regla_1, invalido)

    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12312312, nombre='Juan', apellido='Perez')
        self.assertTrue(self.negS.regla_2(valido))


        # nombre menor a 3 caracteres
        invalido = Socio(dni=12312312, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.negS.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        # valida regla
        valido = Socio(dni=12312312, nombre="Juan", apellido="Perez")
        self.assertTrue(self.negS.regla_2(valido))

        # nombre mayor a 15 caracteres
        invalido = Socio(dni=12312312, nombre="Juan Jose Pedro Alberto", apellido="Perez")
        self.assertRaises(LongitudInvalida, self.negS.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        # valida regla
        valido = Socio(dni=12312312, nombre="Juan", apellido="Perez")
        self.assertTrue(self.negS.regla_2(valido))

        # apellido menor a 3 caracteres
        invalido = Socio(dni=12312312, nombre="Juan", apellido="P")
        self.assertRaises(LongitudInvalida, self.negS.regla_2, invalido)


    def test_regla_2_apellido_mayor_15(self):
        # valida regla
        valido = Socio(dni=12312312, nombre="Juan", apellido="Perez")
        self.assertTrue(self.negS.regla_2(valido))

        # apellido mayor a 15 caracteres
        invalido = Socio(dni=12312312, nombre="Juan", apellido="Perez Fernandez Lopez demaria")
        self.assertRaises(LongitudInvalida, self.negS.regla_2, invalido)

    def test_regla_3(self):
       # valida regla
        socio = Socio(dni=21456789, nombre="Victor", apellido="Demaria")
        self.negS.alta(socio)
        self.assertTrue(self.negS.regla_3())

        # número de socios mayor a 2
        socio = Socio(dni=12788653, nombre="Ayelen", apellido="Demaria")
        self.negS.alta(socio)
        self.assertRaises(MaximoAlcanzado, self.negS.regla_3)

    def test_baja(self):
        pass

    def test_buscar(self):
        pass

    def test_buscar_dni(self):
        pass

    def test_todos(self):
        pass

    def test_modificacion(self):
        pass

if __name__ == "__main__":
    test = TestsNegocio()
    test.setUp()
    test.test_alta()
    test.test_regla_1()
    test.test_regla_2_nombre_menor_3()
    test.test_regla_2_nombre_mayor_15()
    test.test_regla_2_apellido_menor_3()
    test.test_regla_2_apellido_mayor_15()
    test.test_regla_3()
    test.tearDown()
