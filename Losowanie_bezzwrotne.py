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

table = [
    ["Liczba studentów: ", n],
    ["Szczęśliwe numerki w pierwszym tygodniu zajęć to: ", r[0:3]],
    ["Szczęśliwe numerki w drugim tygodniu zajęć to: ", r[3:6]],
    ["Szczęśliwe numerki w trzecim tygodniu zajęć to: ", r[6:9]]
]

print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
