from ukol11 import tah_hrace
from ukol12 import tah_pocitace
from ukol9 import vyhodnot

pole = 20*"-"

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
    pole = tah_pocitace(pole)
    vysledek = vyhodnot(pole)
    if vysledek == "x":
        print("vyhrál jsi!")
        break
    elif vysledek == "o":
        print("Počítač vyhrál")
        break

# rad.n@centrum.cz
# - vytvořit si repo přímo na githubu a pushovat tam úkoly
# - mrknout na nástroj "dbg", lze vkládat mezi řádky a kontrolovat jestli proměnná
# vypadá jak má
