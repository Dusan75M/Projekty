vyska = input("Zadej svou výšku v metrech: ")
vaha = input("Zadej svou váhu v kilogramech: ")
jmeno = input("Zadej svoje jméno: ")

bmi = int(vaha) / float(vyska) ** 2

print("=" * 20)
print("Jméno:", jmeno, "BMI:", bmi)