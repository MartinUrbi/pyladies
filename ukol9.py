#pole = "------ooo-----------"          # je třeba házet před funkci (jako globální proměnnou), abych ji pak mohl mimo funkci i volat

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

#print(vyhodnot(pole))
