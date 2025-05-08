x = 0
y = 1
vysledky = []
delka_rady = 15

while delka_rady > 0:
    z = x
    vysledky.append(z)
    delka_rady -= 1
    x = y
    y = z + x

print(f"Fibonacci: {vysledky}")
