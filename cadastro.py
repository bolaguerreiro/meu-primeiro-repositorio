pessoa = {"nome": "Ricardo", "cidade": "Sao Jose", "profissao": "administrativo"}
print(pessoa)
pessoa.update({"idade": 61})
print(pessoa)   
for chave, valor in pessoa.items():
    print(chave, valor)