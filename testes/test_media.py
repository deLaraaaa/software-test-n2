from stat_funcs import StatsN2
import pytest
from conftest import *


def test_media(lista):
    res = StatsN2.media(lista)
    assert res == 2


def test_media_zero():
    res = StatsN2.media(0)
    assert res == 0


@pytest.mark.xfail(reason="esperado falhar")
def test_media_fail(lista):
    res = StatsN2.media(lista)
    assert res == 1


@pytest.mark.parametrize("test_par,esperado", [
    ([1, 1, 2, 3], 1.75)
])
def test_media_par(test_par, esperado):
    res = StatsN2.media(test_par)
    assert res == 1.75
