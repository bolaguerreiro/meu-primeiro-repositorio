def e_bisexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

print(e_bisexto(2000))
print(e_bisexto(1900))
print(e_bisexto(2024))
print(e_bisexto(2023))
print(round(calcular_imc(81, 1.76),2))
print(round(calcular_imc(80, 1.80),2))

