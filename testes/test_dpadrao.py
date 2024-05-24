from conftest import *
from stat_funcs import StatsN2
import pytest


def test_dpadrao():
    res = StatsN2.dpadrao(0.6666666666666666)
    assert res == 0.816496580927726


@pytest.mark.xfail(reason="esperado falhar")
def test_dpadrao_fail():
    res = StatsN2.dpadrao(0.6666666666666666)
    assert res == 1


@pytest.mark.parametrize("lista_par,esperado", [
    (0.9166666666666666, 2)
])
def test_dpadrao_par(lista_par, esperado):
    res = StatsN2.dpadrao(lista_par)
    assert res == 0.9574271077563381
