class Estadistica:
    def __init__(self, numeros):
        self.numeros = numeros
    def frecc_numeros(self):
        frecuencia = {}
        for numero in self.numeros:
            if numero in frecuencia:
                frecuencia[numero] += 1
            else:
                frecuencia[numero] = 1
        return frecuencia
    def moda(self):
        frecuencia = self.frecc_numeros()
        max_f = max(frecuencia.values())
        moda = [num for num, freq in frecuencia.items() if freq == max_f]
        return moda
    def histograma(self):
        frecuencia = self.frecc_numeros()
        print("Histograma:")
        for numero, freq in frecuencia.items():
            print(f"{numero}: {'*' * freq}")

numeros = [1, 2, 3, 4, 5, 2, 4, 3, 1, 2, 2, 5, 5, 2]
estadisticas = Estadistica(numeros)

frecuencias = estadisticas.frecc_numeros()
print("Números:", frecuencias)

estadisticas.histograma()