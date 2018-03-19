from unittest import TestCase

from Calculadora import Calculadora

class CalculadoraTest(TestCase):
    def test_leer(self):
        self.assertEqual(Calculadora().leer(""),0,"Cadena Vacia")
