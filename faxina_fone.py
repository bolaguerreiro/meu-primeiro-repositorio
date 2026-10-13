import re, csv

with open("contatos.csv", "r", encoding="utf-8") as arquivo:
    for contato in csv.DictReader(arquivo):
        telefone = contato.get("telefone")
        so_telefone = re.sub(r"\D", "", telefone)
        valido = re.fullmatch(r"48\d{8,9}", so_telefone)
        if valido:
            print(contato["nome"], "|", contato["telefone"], "->", so_telefone)
        else:
            print(f"Telefone inválido: {so_telefone}")    
