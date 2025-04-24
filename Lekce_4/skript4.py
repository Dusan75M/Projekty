samohlasky = 'aeiouáéíóú'
souhlasky = 'bcčdďfghjklmnňprřsštťvzžcdž'
vysledky = {'souhlasky': 0, 'samohlasky': 0}
veta = 'Zvuk řeči je produkován otevřenou konfigurací vokálního traktu'

for znak in veta.lower():
    if znak in samohlasky:
        vysledky['samohlasky'] += 1
    elif znak in souhlasky:
        vysledky['souhlasky'] += 1

print("Počet souhlásek:", vysledky['souhlasky'], "| Počet samohlásek:", vysledky['samohlasky'], ".")
  