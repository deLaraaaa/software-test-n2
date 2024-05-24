from conftest import *
from stat_funcs import StatsN2
import pytest


def test_media_ponderada(lista):
    res = StatsN2.media_ponderada(lista, [2, 6, 6, 2])
    assert res == 2


@pytest.mark.xfail(reason="esperado falhar")
def test_media_ponderada_fail(lista):
    res = StatsN2.media_ponderada(lista, [2, 6, 2])
    assert res == 1


@pytest.mark.parametrize("lista_par,pesos_par,esperado", [
    ([1, 1, 2, 3], [2, 2, 2, 4], 2)
])
def test_media_ponderada_par(lista_par, pesos_par, esperado):
    res = StatsN2.media_ponderada(lista_par, pesos_par)
    assert res == 2
