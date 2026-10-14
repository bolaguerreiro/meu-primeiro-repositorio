alunos = [("Joao", 7.5), ("Maria", 8.0), ("Pedro", 9.0), ("Ana", 6.5), ("Carlos", 4.0)]
por_notas = sorted(alunos, key=lambda aluno: aluno[1], reverse=True)
print("Alunos ordenados por notas (decrescente):")
for aluno in por_notas:
    print(f"{aluno[0]}: {aluno[1]}")
aprovados = list(filter(lambda aluno: aluno[1] >= 7, alunos))
print("Alunos aprovados:") 
for aluno in aprovados:
    print(f"{aluno[0]}: {aluno[1]}")
