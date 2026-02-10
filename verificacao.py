num = float(input('Digite o Número: '))
resultado = ("Positivo" * (num > 0)) + \
("Negativo" * (num < 0)) + \
("Zero" * (num == 0))

print("Classificação: ", resultado)