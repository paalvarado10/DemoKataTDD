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
        elif len(cadena)==1:
            return float (cadena)
        else:
            numeros = cadena.split(",")
            minimo = 10000
            for num in numeros:
                if(float(num)<minimo):
                    minimo=float(num)
            return minimo
