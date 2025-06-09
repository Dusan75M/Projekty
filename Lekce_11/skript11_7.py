import csv

jmeno_souboru = 'muj_soubor.csv'

zadane_hodnoty = [
    [10, "a1", 1],
    [12, "a2", 3],
    [14, "a3", 5],
    [16, "a4", 7],
    [18, "a5", 9]
]

def zapis_csv(jmeno, hodnoty):
    with open(jmeno, mode="w", encoding="UTF-8") as nove_csv:
        zapisovac = csv.writer(nove_csv)
        zapisovac.writerows(hodnoty)

def precti_csv(jmeno):
    with open(jmeno, mode="r", encoding="UTF-8") as cteni_csv:
        cteni = csv.reader(cteni_csv, delimiter=";")
        vystup = tuple(cteni)
        return vystup

zapis_csv(jmeno_souboru, zadane_hodnoty)
vystup = precti_csv(jmeno_souboru)

print(f"Obsah: {vystup}")
