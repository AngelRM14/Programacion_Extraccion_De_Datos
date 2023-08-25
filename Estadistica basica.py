"""
Miguel Angel Ruiz Martinez
951
19 de Agosto del 2023
Cree una clase llamada Estadística que contiene como atributo una lista de
números naturales la cual puede contener repetidos. Debe contener los siguientes métodos:
a) Frecuencia de Números. Dada la lista, devuelve un diccionario con el número de veces que
aparece cada número en la lista.
b) Moda. Dada la lista, devuelva la moda de la lista (el valor más repetido). Puedes usar la
función anterior como ayuda.
c) Histograma. Dada la lista, muestra el histograma de la lista. Puedes reusar los métodos
anteriores.
"""
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