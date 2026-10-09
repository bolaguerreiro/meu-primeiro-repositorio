aluno = [
    {"nome": "Ricardo","nota": 8.5},
    {"nome": "Maria","nota": 9.5},
    {"nome": "Joao","nota": 6.5}
]
contador = 0
for a in aluno:
    if a["nota"] >= 7:
        print(f"{a['nome']} foi aprovado com nota {a['nota']}")
        contador += 1
    else:
        print(f"{a['nome']} foi reprovado com nota {a['nota']}")
print(f"Total de alunos aprovados: {contador}")       