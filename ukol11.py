from ukol10 import tah
#pole = 20*"-"

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
                return tah(pole, cislo_policka, "x")
            elif pole[cislo_policka] != "-":
                print("Kuk! Tohle pole už je obsazené!")


#print(tah_hrace(pole))
