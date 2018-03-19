from unittest import TestCase

from Calculadora import Calculadora

class CalculadoraTest(TestCase):
    def test_leer(self):
        self.assertEqual(Calculadora().leer(""),0,"Cadena Vacia")


    def test_leer_un_numero(self):
        self.assertEqual(Calculadora().leer("1"),1,"Un numero")
        self.assertEqual(Calculadora().leer("2"), 1, "Un numero")


    def test_leer_dos_numero(self):
        self.assertEqual(Calculadora().leer("1,2"),2,"Un numero")


    def test_minimo(self):
        self.assertEqual(Calculadora().minimo(""),0,"Cadena Vacia")