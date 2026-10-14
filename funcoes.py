def e_bisexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

print(e_bisexto(2000))
print(e_bisexto(1900))
print(e_bisexto(2024))
print(e_bisexto(2023))
<<<<<<< HEAD
print(round(calcular_imc(81, 1.76),2))
print(round(calcular_imc(80, 1.80),2))
=======
print(calcular_imc(81, 1.76))
print(calcular_imc(80, 1.80))
>>>>>>> 3c17d18e67a19fd1b0db899fe1c6f620bd3ac847

