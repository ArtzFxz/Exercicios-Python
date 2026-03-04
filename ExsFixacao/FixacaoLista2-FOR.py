# EXERCICIO FIXACAO LISTA 2 - FOR

frase = input("Digite a sua frase: ")

f = "aeiouAEIOU"

count = 0
for vogal in frase:
    if vogal in f:
        count+= 1

print(f"Sua frase tem {count} vogais")