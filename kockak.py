import random

feldob_szam = int(input("Hány alkalommal legyen feldobás? "))
print()

szamlalo_A = 0

for i in range(0, feldob_szam):

    szam_1 = random.randint(1, 6)
    szam_2 = random.randint(1, 6)
    szam_3 = random.randint(1, 6)
    osszeg = szam_1 + szam_2 + szam_3

    print(f"Dobás: {szam_1} + {szam_2} + {szam_3} = {osszeg}", end="\t")
    if osszeg < 10:
        szamlalo_A += 1
        print("Nyert: Anni")
    else:
        print("Nyert: Panni")

print(f"\nA játék során {szamlalo_A} alkalommal Anni, {feldob_szam-szamlalo_A} alkalommal Panni nyert. ")
