import random
from tabulate import tabulate



szczęśliwe_numerki =[]
i = 0
n = int(input("Podaj liczebność populacji: "))

while i < 1:
    
    r = random.sample(range(1, n+1), 9)

    if szczęśliwe_numerki.count(r) == 0:
        szczęśliwe_numerki.append(r)
        i += 1

a = r[0:3]
b = r[3:6]
c = r[6:9]

table = [
    ["Liczba studentów: ", n],
    ["Szczęśliwe numerki w pierwszym tygodniu zajęć to: ", a],
    ["Szczęśliwe numerki w drugim tygodniu zajęć to: ", b],
    ["Szczęśliwe numerki w trzecim tygodniu zajęć to: ", c]
]

print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
