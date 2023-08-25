class Pensionista:
    def __init__(self, identificador, edad, gastos_mensuales):
        self.identificador = identificador
        self.edad = edad
        self.gastos_mensuales = gastos_mensuales


class GrupoPensionistas:
    def __init__(self):
        self.pensionistas = []

    def agregar_pensionista(self, pensionista):
        self.pensionistas.append(pensionista)

    def mediaGastos(self, identificador):
        for pensionista in self.pensionistas:
            if pensionista.identificador == identificador:
                promedio_gastos = sum(pensionista.gastos_mensuales) / len(pensionista.gastos_mensuales)
                return promedio_gastos
        return None

    def mediaEdad(self):
        edades = [p.edad for p in self.pensionistas]
        return sum(edades) / len(edades)

    def edadesExtremas(self):
        pensionista_menor_edad = min(self.pensionistas, key=lambda p: p.edad)
        pensionista_mayor_edad = max(self.pensionistas, key=lambda p: p.edad)
        return (pensionista_menor_edad, pensionista_mayor_edad)

    def sumaPromedio(self):
        suma = sum(sum(p.gastos_mensuales) / len(p.gastos_mensuales) for p in self.pensionistas)
        return suma

    def mediaMaxima(self):
        max_promedio = max((sum(p.gastos_mensuales) / len(p.gastos_mensuales), p) for p in self.pensionistas)
        return max_promedio

    def gastoPromedio(self, lst):
        gastos_promedio = [(sum(p.gastos_mensuales) / len(p.gastos_mensuales)) for p in self.pensionistas]
        return sorted(gastos_promedio)


# Ejemplo de uso
grupo = GrupoPensionistas()

pensionista1 = Pensionista("1111A", 68, [640, 589, 573])
pensionista2 = Pensionista("2222B", 75, [700, 600, 550])
pensionista3 = Pensionista("3333C", 60, [800, 500, 600])

grupo.agregar_pensionista(pensionista1)
grupo.agregar_pensionista(pensionista2)
grupo.agregar_pensionista(pensionista3)

print(grupo.mediaGastos("1111A"))
print(grupo.mediaEdad())
print(grupo.edadesExtremas())
print(grupo.sumaPromedio())
print(grupo.mediaMaxima())
print(grupo.gastoPromedio())
