with open("diario.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Acrescentando mais uma linha.\n")
    arquivo.write("Colocando mais uma linha no arquivo.\n")
    arquivo.write("Mais uma linha para o arquivo.\n")
with open("diario.txt", "r", encoding="utf-8") as arquivo:  
    conteudo = arquivo.read()
    print(conteudo)
    