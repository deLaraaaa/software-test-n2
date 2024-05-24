from conftest import *
from stat_funcs import StatsN2
import pytest


def test_unimodal(lista):
    res = StatsN2.unimodal(lista)
    assert res == 2


def test_unimodal_not():
    res = StatsN2.unimodal([1, 2, 3])
    assert res == "Não é unimodal"


@pytest.mark.xfail(reason="esperado falhar")
def test_unimodal_fail(lista):
    res = StatsN2.unimodal(lista)
    assert res == 1


@pytest.mark.parametrize("lista_par,esperado", [
    ([1, 1, 2, 3], 1)
])
def test_unimodal_par(lista_par, esperado):
    res = StatsN2.unimodal(lista_par)
    assert res == 1
