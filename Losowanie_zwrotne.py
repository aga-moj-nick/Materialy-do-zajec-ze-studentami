import random
from tabulate import tabulate


szczęśliwe_numerki =[]
i = 0
n = int(input("Podaj liczebność populacji: "))

while i < 3:
    
    r = random.sample(range(1, n+1), 3)

    if szczęśliwe_numerki.count(r) == 0:
        szczęśliwe_numerki.append(r)
        i += 1


table = [
    ["Liczba studentów: ", n],
    ["Szczęśliwe numerki w pierwszym tygodniu zajęć to: ", szczęśliwe_numerki[0]],
    ["Szczęśliwe numerki w drugim tygodniu zajęć to: ", szczęśliwe_numerki[1]],
    ["Szczęśliwe numerki w trzecim tygodniu zajęć to: ", szczęśliwe_numerki[2]]
]

print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
