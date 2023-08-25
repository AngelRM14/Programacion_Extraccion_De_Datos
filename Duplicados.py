"""
Miguel Angel Ruiz Martinez
951
19 de Agosto del 2023
Dada una lista de números enteros, retorna True si al menos un
valor aparece dos veces, y Falso si todos los elementos son distintos."""

import pytest
from funciones_duplicados import duplicados

def test_duplicados():
    assert duplicados([1,2,3,1])==True
    assert duplicados([1,2,3])==False

@pytest.mark.parametrize("nums, res",
                         [
                             ([1,2,3,1], True),
                             ([1,2,3], False),
                             ([1,1,3,4,5], True)
                         ])

def test_duplicados_parametrizado(nums, res):
    assert duplicados(nums)==res