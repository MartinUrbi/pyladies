
def tah(pole, cislo_policka, symbol):
    """
    Vrátí herní pole s daným symbolem umístěným na danou pozici
    """

    return pole[:cislo_policka] + symbol + pole[cislo_policka +1:]
# vrací začátek řetězce + cislo_policka nahrazené symbolem ("x" nebo "o" a )
# + zbytek řetězce +1 pole, které vzal ten symbol
