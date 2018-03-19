_author_ = 'Pablo Alvarado';

class Calculadora:
    def leer(self,cadena):
        if cadena=="":
            return 0
        else:
            numeros = cadena.split(",")
            return len(numeros)


    def minimo(self,cadena):
        if cadena=="":
            return 0
        else:
            return float(cadena)
