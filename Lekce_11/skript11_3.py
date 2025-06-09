# Nezapomeň nahrát knihovnu, jinak soubor nevytvoříš
import csv

osoba_1 = {"jmeno": "Matous", "prijmeni": "Pokoj", "vek": "28"}
osoba_2 = {"jmeno": "Petr", "prijmeni": "Svetr", "vek": "27"}

# ... nachystáš nový soubor pro zápis
nove_csv = open("druhy_tabulkovy_soubor.csv", mode="w")

# ... z existujících klíčů si vytvoříš záhlaví
zahlavi = osoba_1.keys()

# ... nachystáš si nový zapisovač, kterému nastavíš parametr "fieldnames"
zapisovac = csv.DictWriter(nove_csv, fieldnames=zahlavi)

# ... nejprve zapíšeš záhlaví
zapisovac.writeheader()

# ... následně oba údaje
zapisovac.writerow(osoba_1)
zapisovac.writerow(osoba_2)

# ... nakonec soubor ukončíš
nove_csv.close()

# pomocí kontextového manažeru
with open("druhy_tabulkovy_soubor.csv", mode="w") as nove_csv:
    zahlavi = osoba_1.keys()
    zapisovac = csv.DictWriter(nove_csv, fieldnames=zahlavi)

    zapisovac.writeheader()
    zapisovac.writerow(osoba_1)
    zapisovac.writerow(osoba_2)