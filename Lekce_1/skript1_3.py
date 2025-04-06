mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000

sleva_merc = 5000
print("Sleva na Mercedes:", sleva_merc)

cena_2_merc = 2 * mercedes
print("Cena za dva Mercedesy je:", cena_2_merc)

cena_merc_a_rolls = mercedes + rolls_royce
print("Cena za Mercedes a Rolls-Royce:", cena_merc_a_rolls)

cena_2_rolls_s_vybavou = 2 * (rolls_royce + vybava)
print("Cena za dva Rolls-Royce s příplatkovou výbavou:", cena_2_rolls_s_vybavou)

cena_merc_s_vybavou = mercedes + vybava
print("Cena za Mercedes s příplatkovou výbavou:", cena_merc_s_vybavou)

merc_se_slevou = mercedes - sleva_merc
print("Cena za Mercedes po slevě", merc_se_slevou)