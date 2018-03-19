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
            if(numeros[0]>numeros[1]):
                return float(numeros[1])
            else:
                return float(numeros[0])

