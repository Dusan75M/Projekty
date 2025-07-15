import sys

def formatuj_jmeno(jmeno):
    print(f"Uživatel {jmeno} spouští program")


if len(sys.argv) != 2:
    print(
        "Pro spuštění chybí argument 'jmeno',",
        "Zapiš: python skript11_6.py 'jmeno'", sep="\n"
    )
else:
    formatuj_jmeno(sys.argv[1])
