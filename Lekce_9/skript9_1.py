jmeno_souboru = "novy_soubor.txt"
pozdrav = "Ahoj, toto je první zápis do textového souboru"

txt_soubor = open(jmeno_souboru, mode="w")
txt_soubor.write(pozdrav)

# řádné zavření souboru
txt_soubor.close()

txt_soubor = open("novy_soubor.txt", mode="r")
obsah_txt = txt_soubor.read()
print(obsah_txt)
txt_soubor.close()

druhy_radek = "Ted pridavas druhy radek"

txt_soubor = open("novy_soubor.txt", mode="r+")
obsah_txt = txt_soubor.read()
txt_soubor.write(druhy_radek)

txt_soubor.close()

treti_radek = "Toto je treti radek tveho puvodniho souboru souboru ^.^"

txt_soubor = open("novy_soubor.txt", mode="a")
txt_soubor.write(treti_radek)
txt_soubor.close()

with open("dalsi_soubor.txt", mode="w") as txt_soubor:
    txt_soubor.write("Nový txt s kontextovým manažerem!")