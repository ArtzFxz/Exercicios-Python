total = 0
quantidade = 0

while True:
    preco = float(input("Digite o preço do produto (0 para encerrar): "))

    if preco == 0:
        break

    elif preco < 0:
        print("Valor Inválido")

    else:  # maior que 0
        total += preco
        quantidade += 1

if quantidade > 0:
    media = total / quantidade
else:
    media = 0

print("\n--- Fechamento do Caixa ---")
print(f"Total da compra: R$ {total:.2f}")
print(f"Quantidade de itens: {quantidade}")
print(f"Média por produto: R$ {media:.2f}")

# BÔNUS
if quantidade > 0:
    pagamento = int(input("\nForma de pagamento (1 - Dinheiro / 2 - Cartão): "))

    if pagamento == 1:
        desconto = total * 0.05
        total -= desconto
        print("Pagamento em Dinheiro - 5% de desconto aplicado.")
        print(f"Total com desconto: R$ {total:.2f}")

    elif pagamento == 2:
        print("Pagamento em Cartão - Sem desconto.")
        print(f"Total final: R$ {total:.2f}")

    else:
        print("Opção inválida.")
