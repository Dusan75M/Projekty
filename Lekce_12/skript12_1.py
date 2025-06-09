import requests
from bs4 import BeautifulSoup as bs

def nacti_obsah_stranky(url):
  obsah = requests.get(url)
  if obsah.status_code == 200:
    return bs(obsah.text, features="html.parser")
  else:
    return None

def ziskej_cenu_zlata(rozdeleny_text):
  element_span = rozdeleny_text.find("span", {"class": "price-section__current-value"})
  if element_span:
    return element_span.get_text()
  else:
    return None

def main():
  url = "https://markets.businessinsider.com/commodities/gold-price"
  obsah_stranky = nacti_obsah_stranky(url)
  if obsah_stranky is None:
    print("Nedostupný HTML objekt")
    return None
  else:
    cena_zlata = ziskej_cenu_zlata(obsah_stranky)
    if cena_zlata is None:
      print("Nedostupná cena")
      return None
    else:
      print(f"Aktuální cena zlata $: {cena_zlata}")
      
main()
