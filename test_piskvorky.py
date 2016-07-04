import piskvorky
import ai
import pytest

def test_tah():
    pole = ai.tah_pocitace('--------------------')
    assert len(pole) == 20
    assert pole.count('o') == 1
    assert pole.count('-') == 19


def test_tah_chyba():
    with pytest.raises(ValueError):
        ai.tah_pocitace('oxoxoxoxoxoxoxoxoxox')
