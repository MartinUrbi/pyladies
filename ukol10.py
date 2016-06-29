# vždy je třeba vyhodit proměnnou, která se bude měnit a vstupuje v jakémkoli stavu před funkci
# (tady je to "pole")

pole = 20*"-"

def tah(pole, cislo_policka, symbol):
    """
    Vrátí herní pole s daným symbolem umístěným na danou pozici
    """

    return pole[:cislo_policka] + symbol + pole[cislo_policka +1:]
# vrací začátek řetězce + cislo_policka nahrazené symbolem ("x" nebo "o" a )
# + zbytek řetězce +1 pole, které vzal ten symbol

# print(tah(pole, 15,"x"))            # můžu zakomentovat, protože printy si volám v úkolu13.
