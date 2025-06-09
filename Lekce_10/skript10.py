zadany_slovnik = {
   'jmeno':'Pepa',
   'prijmeni': 'Novak',
   'rok_narozeni': 1990,
   'email': 'pepa.novak@seznam.cz'
}

def obsahuje_udaje(klic, hodnota, slovnik):
    try:
        klic in slovnik[klic]
    except KeyError:
        print(f"Klíč: {klic} nenalezen.")
        vysledek = False
    else:
        print(f"Klíč: {klic} nalezen.")
        if hodnota == slovnik[klic]:
            vysledek = True
        else:
            print(f"Hodnota: {hodnota} nenalezena.")
            vysledek = False
    return vysledek

vystup_1 = obsahuje_udaje(klic="jmeno", hodnota="Pepa", slovnik=zadany_slovnik)
vystup_2 = obsahuje_udaje(klic="jmeno", hodnota="Marek", slovnik=zadany_slovnik)
vystup_3 = obsahuje_udaje(klic="name", hodnota="John", slovnik=zadany_slovnik)

print(vystup_1, vystup_2, vystup_3, sep="\n")
