vstupni_text = "Ahoj všem, tady Engeto"

def zdvojnasob_znaky(text):
    zdvojene = list()
    for znak in text:
        znak *= 2
        zdvojene.append(znak)
    return(zdvojene)

vystupni_text = zdvojnasob_znaky(vstupni_text)
vysledek = "".join(vystupni_text)

print("Zdvojené znaky:", vysledek)
