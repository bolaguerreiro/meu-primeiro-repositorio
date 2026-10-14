def e_bisexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

print(e_bisexto(2000))
print(e_bisexto(1900))
print(e_bisexto(2024))
print(e_bisexto(2023))
print(calcular_imc(81, 1.76))
print(calcular_imc(80, 1.80))

