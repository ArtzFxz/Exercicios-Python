# for i in range(1):
#     n1 = float(input("Digite um número: "))
#     n2 = float(input("Digite um segundo número: "))
#     n3 = float(input("Digite um terceiro número: "))
#     n4 = float(input("Digite um quarto número: "))
#     n5 = float(input("Digite um quinto número: "))

#     soma = n1 + n2 + n3 + n4 + n5
#     media = (n1 + n2 + n3 + n4 + n5) / 5

#     print(f"A soma dos cinco número é: {soma} e a média é: {media}")



soma = 0
repetir = 5
x = len(range(repetir))

for i in range(5):
    num = float(input(f"Digite o {i+1} número: "))
    soma += num

media = (soma / x)

print(f"\nSoma total: {soma}")
print(f"Media dos números: {media}")