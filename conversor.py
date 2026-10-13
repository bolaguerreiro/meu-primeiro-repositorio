import csv, json

with open("clientes.csv", newline="", encoding="utf-8") as arquivo:
    conversor = list(csv.DictReader(arquivo))

ativos =[]

for c in conversor:
    if c["ativo"] == "True":
        ativos.append(c)

with open("ativos.json", "w", encoding="utf-8") as arquivo:
    json.dump(ativos, arquivo, indent=2, ensure_ascii=False)

print(len(ativos), "clientes ativos foram salvos no arquivo ativos.json")