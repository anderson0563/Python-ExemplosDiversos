class CalculoFibonacci:
    def __init__(self, nTermoSerie):
        self.nTermoSerie = nTermoSerie
    
    def recursivo(self, i):
        if i==1 or i==0:
            return i
        else:
            return self.recursivo(i-1) + self.recursivo(i-2)
    
    def calculo(self):
        return self.recursivo(self.nTermoSerie)


class CalculoFatorial:
    def __init__(self, numero):
        self.numero = numero
    
    def recursivo(self, i):
        if i==1 or i==0:
            return 1
        else:
            return i * self.recursivo(i-1)
    
    def calculo(self):
        return self.recursivo(self.numero)