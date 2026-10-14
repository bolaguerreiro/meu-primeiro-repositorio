def media(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

def desconto(preco, percentual=10):
    return preco * (1 - percentual / 100)

def situacao(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperacao"
    else:
        return "Reprovado"


notas = [7.5, 8.0, 9.0, 6.5, 4.0]
print("Media das notas:", media(notas))
print("Preco com desconto:", desconto(100, 15))
print("Preco com desconto padrao:", desconto(100))
print("Preco sem desconto:", desconto(preco=100, percentual=0)) #nomeado
print("Situacao do aluno com nota 8:", situacao(8))
print("Situacao das notas: ", situacao(notas[0]), situacao(notas[1]), situacao(notas[2]), situacao(notas[3]), situacao(notas[4]))