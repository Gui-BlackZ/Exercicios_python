class tabuada:
    def __init__(self,numero):
        self.valor = numero
        self._resultado = 0
   
    def soma(self):
        for i in range(1,11):
            self._resultado = self.valor + i
            print("{} + {} = {}".format(self.valor,i,self._resultado))
 
    def subtracao(self):
        for i in range(1,11):
            self._resultado = self.valor - i
            print("{} - {} = {}".format(self.valor,i,self._resultado))
 
    def multiplacao(self):
        for i in range(1,11):
            self._resultado = self.valor * i
            print("{} * {} = {}".format(self.valor,i,self._resultado))
       
    def divisao(self):
        for i in range(1,11):
            self._resultado = self.valor / i
            print("{} / {} = {}".format(self.valor,i,self._resultado))