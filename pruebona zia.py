class Estadistica():

    def __init__(self, numeros):
        self.numeros = numeros

    def FrecuenciaNumeros(self):
        dic = {}
        for value in self.numeros:
            if value in dic:
                dic[value]+=1
            else:
                dic[value] = 1
        return dic

    def Moda(self):
        dic = self.FrecuenciaNumeros()
        maximo = 0
        moda = 0
        for value in dic:
            if dic[value] > maximo:
                maximo = dic[value]
                moda = value
        return moda

    def Histograma(self):
        dic = self.FrecuenciaNumeros()
        for value in dic:
            print(value, "*" * dic[value])

lista = Estadistica([1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1])
print(lista.FrecuenciaNumeros())
print(lista.Moda())
print(lista.Histograma())