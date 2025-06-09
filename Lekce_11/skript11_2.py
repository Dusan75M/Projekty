# Nezapomeň nahrát knihovnu, jinak soubor nevytvoříš
import csv

hlavicka = ["jmeno", "prijmeni", "vek"]
osoba_1 = ["Matous", "Pokoj", "28"]
osoba_2 = ["Petr", "Svetr", "27"]

# ... nachystáš nový soubor pro zápis
nove_csv = open("prvni_tabulkovy_soubor.csv", mode="w")

# ... vytvoříš zapisovací objekt, který do souboru zapíše údaje
zapisovac = csv.writer(nove_csv)

# ... nejprve zapíšeš záhlaví
zapisovac.writerow(hlavicka)

# ... potom první údaj
zapisovac.writerow(osoba_1)

# ... druhý údaj
zapisovac.writerow(osoba_2)

# pomocí writerows
zapisovac.writerows(
   ( 
       hlavicka,
       osoba_1,
       osoba_2
   )
)

# ... nakonec objekt a soubor uzavřeš
nove_csv.close()

# pomocí kontextového manažeru
with open("prvni_tabulkovy_soubor.csv", mode="w") as nove_csv:
   zapisovac = csv.writer(nove_csv)
   zapisovac.writerows(
      (
          hlavicka,
          osoba_1,
          osoba_2
      )
  )