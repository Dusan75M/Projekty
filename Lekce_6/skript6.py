import random

moznosti = ['kamen', 'nuzky', 'papir']
hrac_volby = list()
pocitac_volby = list()

while len(hrac_volby) < 3:
    hrac_volby.append(random.choice(moznosti))
    pocitac_volby.append(random.choice(moznosti))

#print(hrac_volby)    
#print(pocitac_volby)

for hrac, pocitac in zip(hrac_volby, pocitac_volby):
    if hrac == pocitac:
        vysledek = "Remíza!"
        print("Výsledek:", vysledek)
    elif hrac == "kamen" and pocitac == "nuzky":
        vysledek = "Vyhrává hráč!"
        print("Výsledek:", vysledek)
    elif hrac == "nuzky" and pocitac == "papir":
        vysledek = "Vyhrává hráč!"
        print("Výsledek:", vysledek)
    elif hrac == "papir" and pocitac == "kamen":
        vysledek = "Vyhrává hráč!"
        print("Výsledek:", vysledek)
    else:
        vysledek = "Vyhrává počítač!"
        print("Výsledek:", vysledek)
