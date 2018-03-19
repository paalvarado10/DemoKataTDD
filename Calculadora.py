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


    def max(self, cadena):
        if cadena=="":
            return 0
        elif len(cadena.split(","))==1:
            return float(cadena)
        else:
            numeros = cadena.split(",")
            max = 0
            for num in numeros:
                if(float(num)>max):
                    max=float(num)
            return max

    def prom(self, cadena):
        if cadena =="":
            return 0
        elif len(cadena.split(","))==1:
            return float(cadena)
        else:
            numeros = cadena.split(",")
            promedio = 0
            i=0
            for num in numeros:
                promedio += float(num)
                i=i+1
            return promedio/i