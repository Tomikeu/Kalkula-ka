x = input("Napiš číslo X\n")
y = input("Napiš číslo Y\n")
z = input("Vyber znaménko\n1. Sčítání\n2. Odečítání\n3. Násobení\n4. Dělení\n5. Mocnina\n6. Odmocnina")

x = (int(x))
y = (int(y))

if z == "Sčítání" or "1." or "1. Sčítání" or "1" or "scitani":
    m = (x + y)
    m = (str(m))
    print("Výsledek je " + m)
elif z == "Odečítání" or "2." or "2. Odečítání" or "2" or "odecitani":
    m = (x - y)
    m = (str(m))
    print("Výsledek je " + m)
elif z == "Násobení" or "3." or "3. Násobení" or "3" or "nasobeni":
    m = (x * y)
    m = (str(m))
    print("Výsledek je " + m)
elif z == "Dělení" or "4." or "4. Dělení" or "4" or "deleni":
    m = (x / y)
    m = (str(m))
    print("Výsledek je " + m)
elif z == "Mocnina" or "5." or "5. Mocnina" or "5" or "mocnina":
    m = (x ** y)
    m = (str(m))
    print("Výsledek je " + m)
elif z == "Odmocnina" or "6." or "6. Odmocnina" or "6" or "odmocnina":
    m = (x * 1 / y)
    m = (str(m))
    print("Výsledek je " + m)