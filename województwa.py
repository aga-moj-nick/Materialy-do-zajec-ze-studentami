import random
from tabulate import tabulate


województwa =[]
i = 0
n = int(input("Podaj liczbę zespołów: "))

while i < 1:
    
    r = random.sample(range(1, n+1), n)

    if województwa.count(r) == 0:
        województwa.append(r)
        i += 1

table = [
    ["Liczba zespołów: ", n],
    ["Województwo kujawsko-pomorskie: ", r[0]],
    ["Województwo pomorskie: ", r[1]],
    ["Województwo śląskie: ", r[2]],
    ["Województwo lubelskie: ", r[3]],
    ["Województwo małopolskie: ", r[4]],
    ["Województwo wielkopolskie: ", r[5]],
    ["Województwo zachodniopomorskie: ", r[6]],
    ["Województwo dolnośląskie: ", r[7]]
]

print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
