import tah
import ai

pole = 20*"-"

def vyhodnot(pole):

    "Vyhodnotí výhru hráče, počítače, nebo remízu."

    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:       # stačí se zeptat na pomlčku, protože "xxx" a "ooo" si to zkontroluje v předchozích krocích
        return "!"
    else:
        return "-"


def tah_hrace(pole):
    while True:
        try:
            cislo_policka = int(input("Na které políčko chceš hrát?"))
        except ValueError:
            print("Tohle nebylo číslo :/")
        else:
            if cislo_policka <0 or cislo_policka >=20:      # jde použít taky >=len(pole)
                print("Na tohle pole hrát nejde!")
                continue        # pustí cyklus znova, supr věc :)
            elif pole[cislo_policka] == "-":
                return tah.tah(pole, cislo_policka, "x")
            elif pole[cislo_policka] != "-":
                print("Kuk! Tohle pole už je obsazené!")

def piskvorky1d(pole):
    while True:         # velmi častý případ použití while, prostě dokud podmínka bude platit!
        print("POLE:", pole)
        pole = tah_hrace(pole)
        vysledek = vyhodnot(pole)
        if vysledek == "x":
            print("Výsledný stav:", pole)
            print("Vyhrál jsi!")
            break
        elif vysledek == "o":
            print("Výsledný stav:", pole)
            print("Počítač vyhrál")
            break
        pole = ai.tah_pocitace(pole)
        vysledek = vyhodnot(pole)
        if vysledek == "x":
            print("vyhrál jsi!")
            break
        elif vysledek == "o":
            print("Počítač vyhrál")
            break

#piskvorky1d(pole)
