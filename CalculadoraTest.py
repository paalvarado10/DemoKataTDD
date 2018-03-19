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

    def test_minimo_un_numero(self):
        self.assertEqual(Calculadora().minimo("1"),1,"Un numero")


    def test_minimo_dos_numeros(self):
        self.assertEqual(Calculadora().minimo("1,2"),1,"Dos numeros ")


    def test_minimo_n_numeros(self):
        self.assertEqual(Calculadora().minimo("2,3,1"),1,"tres numeros ")
        self.assertEqual(Calculadora().minimo("2,4,1,0"),0, "cuatro numeros ")

    def test_max(self):
        self.assertEqual(Calculadora().max(""),0,"Cadena Vacia")

    def test_max_un_numero(self):
        self.assertEqual(Calculadora().max("1"), 1, "Un numero")
        self.assertEqual(Calculadora().max("10"), 10, "Un numero")

    def test_max_dos_numeros(self):
        self.assertEqual(Calculadora().max("1,2"),2,"Dos numeros ")
        self.assertEqual(Calculadora().max("4,2"),4, "Dos numeros ")


    def test_max_n_numeros(self):
        self.assertEqual(Calculadora().max("2,1,3"),3,"tres numeros ")
        self.assertEqual(Calculadora().max("2,1,1,4"),4,"cuatro numeros ")


    def test_promedio(self):
        self.assertEqual(Calculadora().prom(""),0,"Cadena Vacia")


    def test_promedio_un_numero(self):
        self.assertEqual(Calculadora().prom("1"), 1, "Un numero")
        self.assertEqual(Calculadora().prom("10"), 10, "Un numero")


    def test_prom_dos_numeros(self):
        self.assertEqual(Calculadora().prom("2,2"),2,"Dos numeros ")
        self.assertEqual(Calculadora().prom("4,2"),3, "Dos numeros ")

    def test_prom_n_numeros(self):
        self.assertEqual(Calculadora().prom("2,3,1"), 2, "tres numeros ")
        self.assertEqual(Calculadora().prom("2,1,1,4"), 2, "cuatro numeros ")

    def test_array(self):
        self.assertEqual(Calculadora().calculate("2,3,1"),[3,1,3,2], "tres numeros ")

