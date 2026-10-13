import csv

with open("notas.csv", newline="", encoding="utf-8") as arquivo:
    for nome in csv.DictReader(arquivo):
        media = (float(nome["nota1"]) + float(nome["nota2"])) / 2
        print(f"{nome['nome']} - Media: {media:.2f}")
