#import pdb

druh_stromu = "smrk"
pocet_stromu = 150
stari_porostu = 80  # v rocich

def stav_lesa():
#    pdb.set_trace()
    return "Jedná se o {druh}ový porost. Počet stromů je {pocet}, věk porostu je {stari} let.".format(druh = druh_stromu, pocet = pocet_stromu, stari = stari_porostu)

#print(stav_lesa())

stresor = "sucho"
skudce = "kůrovec"

def zdravotni_stav():
    return "Porosty dlouhodobě oslabuje {stresor} a napadá {skudce}. Poškození větrem a dalšími abiotickými činiteli je zanedbatelné.".format(stresor = stresor, skudce = skudce)
