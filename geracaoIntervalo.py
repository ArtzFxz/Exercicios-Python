inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o segundo número: "))

if inicio <= fim:
    passo = 1
else:
    passo = -1

print(f"Números no intervalo entre {inicio} e {fim}")

for i in range(inicio, fim + passo, passo):
    print(i, end=" ")