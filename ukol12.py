from random import randrange
from ukol10 import tah

pole = 20*"-"
def tah_pocitace(pole):
    "vrátí herní pole a zaznamená tah počítače"

    while True:
        pozice = randrange(19)
        if pole[pozice] == "-": #and pole[pozice+1] == "x":
            break
    return tah(pole, pozice, "o")

print(tah_pocitace(pole))
