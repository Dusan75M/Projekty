# Nezapomeň na potřebnou knihovnu
import csv

# Načteš soubor "csv" jako objekt "cteni_csv"
cteni_csv = open("prvni_tabulkovy_soubor.csv")

# Vytvoříš iterovatelný objekt se všemi záznamy ze souboru
cteni = csv.reader(cteni_csv)

# Vypíšeš obsah "csv" souboru s pomocí funkce "tuple"
print(tuple(cteni))

# Ukončíš soubor
cteni_csv.close()

# pomocí kontextového manažeru
with open('prvni_tabulkovy_soubor.csv') as cteni_csv:
    cteni = csv.reader(cteni_csv)
    print(tuple(cteni))