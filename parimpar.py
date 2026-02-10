numero = int(input("Digite um número: "))
resto = numero % 2
resultado = ("Par" * (1 - resto)) + ("Impar" * resto)

print("O numero é: ", resultado)