import csv, re, datetime
from datetime import datetime

limpas = []

with open("sujo.csv", "r", encoding="utf-8") as arquivo:
    for contato in csv.DictReader(arquivo):
        telefone = contato.get("telefone")
        so_telefone = re.sub(r"\D", "", telefone)
        nome = contato.get("nome")
        nome_correto = re.sub(r"\s+", " ",str.title(nome).strip())
        data = contato.get("data")
        data_correta = datetime.strptime(data,"%d/%m/%Y").strftime("%Y/%m/%d")
        valido = re.fullmatch(r"48\d{8,9}", so_telefone)
        if valido:
            print(nome, "|", nome_correto, "->", so_telefone, "->", data_correta)
        else:
            print(f"Telefone inválido: {so_telefone}")
            so_telefone = "Telefone inválido"
        limpas.append({"nome": nome_correto, "telefone": so_telefone, "data": data_correta})

with open("limpo.csv", "w", encoding="utf-8", newline="") as arquivo:
   escritor = csv.DictWriter(arquivo, fieldnames=["nome", "telefone", "data"])
   escritor.writeheader()
   escritor.writerows(limpas)
