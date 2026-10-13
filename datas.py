from datetime import datetime

# data = input("Digite a data de nascimento (dd/mm/aaaa): ")
# data_nascimento = datetime.strptime(data, "%d/%m/%Y")
# idade = datetime.now().year - data_nascimento.year
# print(f"Idade: {idade} anos")
hoje = datetime.now()
natal = datetime(hoje.year, 12, 25)
diferenca = natal - hoje
print(f"Faltam {diferenca.days} dias para o Natal.")
