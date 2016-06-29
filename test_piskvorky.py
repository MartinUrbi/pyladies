import piskvorky

def test_tah():
    pole = piskvorky.tah_pocitace('--------------------')
    assert len(pole) == 20
    assert pole.count('x') == 1
    assert pole.count('-') == 19
