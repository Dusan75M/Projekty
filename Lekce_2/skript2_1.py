vyska = 1.80
vaha = 80
jmeno = "Karel Novák"

bmi = vaha / vyska ** 2

print("Jméno: ", jmeno, " - BMI: ", bmi, ".")

kategorie = []

if bmi < 18.5:
  kategorie.insert(0, "Podvýživa")
elif 18.5 <= bmi < 25:
  kategorie.insert(0, "Zdravá váha")
elif 25 <= bmi < 30:
  kategorie.insert (0, "Mírná nadváha")
elif 30 <= bmi < 40:
  kategorie.insert(0, "Obezita")
else:
  kategorie.insert(0, "Těžká obezita")

print("Jméno: ", jmeno, ", kategorie: ", kategorie, ".")