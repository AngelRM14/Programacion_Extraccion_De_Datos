"""
Miguel Angel Ruiz Martinez
951
19 de Agosto del 2023
Crear una clase llamada GrupoPensionistas la cual tendrá un único atributo una lista o
diccionario de objetos de tipo Pensionista (Elija a conveniencia si una lista o diccionario).
Cada objeto de Pensionista tiene los siguientes atributos: identificador del pensionista
(string), un entero que indica la edad y una serie de gastos mensuales que se guardan
(lista de enteros). El número de gastos mensuales puede variar entre pensionistas. Por ejemplo,
el pensionista con identificador '1111A' se llama 'Carlos' tiene 68 años y tiene 3 gastos mensuales
de 640, 589 y 573.
La clase GrupoPensionistas debe tener los siguientes métodos:

- mediaGastos(identificador) , dado el identificador o índice de un pensionista, devuelva el promedio de
los gastos.
- mediaEdad(), dado todos los pensionados, devuelve el promedio de las edades.
- edadesExtremas(), dado todos los pensionados, devuelva al pensionado con menor y mayor edad en una tupla.
- sumaPromedio(), dado todos los pensionados, devuelva la suma del promedio de los gastos de todos los
pensionistas de la lista.
- mediaMaxima(), dado todos los pensionistas, retorne el mayor promedio de los gastos entre todos los pensionistas
de la lista, su nombre e identificador.
- gastoPromedio(lst), dado todos los pensionistas, devuelve una lista con el gasto promedio de cada persona.
La lista resultante debe estar ordenada de forma ascendente.
"""

class PersonaPensionada:
    def __init__(self, codigo, edad, gastos):
        self.codigo = codigo
        self.edad = edad
        self.gastos = gastos

class GrupoPersonasPensionadas:
    def __init__(self, personas_pensionadas):
        self.personas_pensionadas = personas_pensionadas

    def promedioGastos(self, codigo):
        for persona_pensionada in self.personas_pensionadas:
            if persona_pensionada.codigo == codigo:
                return sum(persona_pensionada.gastos) / len(persona_pensionada.gastos)
        return None

    def promedioEdad(self):
        totalEdad = 0
        for persona_pensionada in self.personas_pensionadas:
            totalEdad += persona_pensionada.edad
        return totalEdad / len(self.personas_pensionadas)

    def edadesExtremas(self):
        edadMenor = 1000
        edadMayor = 0
        for persona_pensionada in self.personas_pensionadas:
            if persona_pensionada.edad < edadMenor:
                edadMenor = persona_pensionada.edad
            if persona_pensionada.edad > edadMayor:
                edadMayor = persona_pensionada.edad
        return edadMenor, edadMayor

    def sumaPromedio(self):
        suma = 0
        for persona_pensionada in self.personas_pensionadas:
            suma += sum(persona_pensionada.gastos) / len(persona_pensionada.gastos)
        return suma

    def promedioMaximo(self):
        maxPromedio = None
        maxValor = 0

        for persona_pensionada in self.personas_pensionadas:
            promedio_actual = sum(persona_pensionada.gastos) / len(persona_pensionada.gastos)

            if promedio_actual > maxValor:
                maxValor = promedio_actual
                maxPromedio = (persona_pensionada.codigo, maxValor)

        return maxPromedio

    def gastoPromedio(self):
        promedioGastos = []
        for persona_pensionada in self.personas_pensionadas:
            promedioGastos.append(sum(persona_pensionada.gastos) / len(persona_pensionada.gastos))
        return sorted(promedioGastos)
persona_pensionada1 = PersonaPensionada('1111A', 68, [640, 589, 573])
persona_pensionada2 = PersonaPensionada('1222A', 80, [250, 552, 223])
persona_pensionada3 = PersonaPensionada('1333A', 75, [140, 202, 910])

grupo_personas = GrupoPersonasPensionadas([persona_pensionada1, persona_pensionada2, persona_pensionada3])
print(grupo_personas.promedioGastos('1111A'))
print(grupo_personas.promedioEdad())
print(grupo_personas.edadesExtremas())
print(grupo_personas.sumaPromedio())
print(grupo_personas.promedioMaximo())
print(grupo_personas.gastoPromedio())
