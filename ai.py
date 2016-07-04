from random import randrange
from tah import tah               # lepší importovat jen 1 funkci nebo vše?

pole = 20*"-"
def tah_pocitace(pole):
    "vrátí herní pole a zaznamená tah počítače"
    if pole.find("-") == -1:
        raise ValueError
    for i in range(50):
        pozice = randrange(19)
        if pole[pozice] == "-" and pole[pozice+1] == "x":       #DOKONČIT!! 
            break
    return tah(pole, pozice, "o")

print(tah_pocitace(pole))
