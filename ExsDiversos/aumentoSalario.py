salario_atual = float(input("Digite o salario atual do colaborador: R$ "))

if salario_atual <= 280:
    percentual = 20
elif salario_atual <= 700:
    percentual = 15
elif salario_atual <= 1500:
    percentual = 10
else:
    percentual = 5

valor_aumento = salario_atual *(percentual / 100)
novo_salario = salario_atual + valor_aumento

print(f"\nSalário antes do reajuste: R$ {salario_atual}")
print(f"Percentual de aumnto aplicado: {percentual}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário, apos o aumento : R$ {novo_salario}")