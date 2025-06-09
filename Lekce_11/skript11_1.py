# bez knihovny nemůžeš pracovat s JSON objekty
import json

chuckuv_slovnik = {
    "jmeno": "Chuck Norris",
    "neuspech": None,
    "kliky": "vsechny",
    "konkurence": False,
    "fanousek": "Łukasz"
}

# funkci 'open' nachystáš objekt v Pythonu
json_soubor = open("prvni_json_soubor.json", mode="w")

# metoda 'dump' uloží objektu do souboru
json.dump(chuckuv_slovnik, json_soubor)

# ... nezapomeň objekt ukončit
json_soubor.close()

#pomocí kontextového manažeru
with open("prvni_json_soubor.json", mode="w") as json_soubor:
   # metoda "dump" uloží objektu do souboru
   json.dump(chuckuv_slovnik, json_soubor)

with open("prvni_json_soubor.json", mode="r") as json_soubor:
   # .. uložím obsah souboru
   obsah_jsonu = json.load(json_soubor)

print(obsah_jsonu)
