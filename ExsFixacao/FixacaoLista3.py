# EXERCICIO FIXACAO LISTA 3

saldo_inicial = 1000.0
checkpoint = saldo_inicial

print("Checkpoint e saldo_inicial são o mesmo objeto?",
      checkpoint is saldo_inicial)

while True:
    auditor = input("Digite o nome do auditor: ")
    
    if "*" in auditor or "#" in auditor:
        print("Nome contém caracteres proibidos (* ou #). Tente novamente.")
    else:
        break

saldo_atual = saldo_inicial

for i in range(1, 5):
    valor = float(input(f"Digite o valor da transição {i}: "))
    
    if valor > 500.0:
        print("Transação de alto valor!")
    
    if valor < 0 and saldo_atual + valor < 0:
        print("Erro: saldo insuficiente. Transação ignorada.")
        continue

    saldo_atual += valor

saldo_final = saldo_atual

print(f"\nSaldo final: R$ {saldo_final:.2f}")
print("Saldo final é o mesmo objeto que checkpoint?", saldo_final is checkpoint)