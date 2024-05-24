from conftest import *
from stat_funcs import StatsN2
import pytest


def test_multimodal():
    res = StatsN2.multimodal([1, 1, 2, 2, 3])
    assert res == [1, 2]


def test_multimodal_not(lista):
    res = StatsN2.multimodal(lista)
    assert res == "Não é multimodal"


@pytest.mark.xfail(reason="esperado falhar")
def test_multimodal_fail(lista):
    res = StatsN2.multimodal([1, 1, 2, 2, 3])
    assert res == [1, 3]


@pytest.mark.parametrize("lista_par,esperado", [
    ([1, 1, 2, 3, 3], [1, 3])
])
def test_multimodal_par(lista_par, esperado):
    res = StatsN2.multimodal(lista_par)
    assert res == [1, 3]
