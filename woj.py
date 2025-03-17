import random
from tabulate import tabulate


i = 0
n = int(input("Podaj liczbę zespołów: "))

r = random.sample(range(1, n+1), n)

wojewodztwa = ["kujawsko-pomorskie", "pomorskie", "śląskie", "lubelskie", "małopolskie", "wielkopolskie", "zachodniopomorskie", "dolnośląskie"]
table = [["Liczba zespołów: ", n]]

for i, w in enumerate(wojewodztwa):
    if (len(r) >= i+1):
        table.append(["Województwo " + w, r[i]])

print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
