"""
Miguel Angel Ruiz Martinez
951
19 de Agosto del 2023
Dado una lista de números enteros y un valor entero (target),
retorna el índice de los dos números que sumados sean igual al target.
Debe asumir que existe siempre una única solución, y que los elementos
no se pueden usar dos veces. Debes retornar una tupla con los índices."""

def indices(nums, target):
    num_indices = {}

    for i, numero in enumerate(nums):
        resultado =target-numero
        if resultado in num_indices:
            return (num_indices[resultado], i)
        num_indices[numero] = i


