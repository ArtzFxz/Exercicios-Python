value = float(input("Digite o valor de sua compra: "))
d1 = value - value * 0.10
d2 = value - value * 0.20
d3 = value - value * 0.30


if value >= 100 and value < 200:
    print(f"Parabéns! Você conseguiu um desconto de 10%, seu produto está custando: {d1:.2f}")
elif value >= 200 and value < 500:
    print(f"Parabéns! Você conseguiu um desconto de 20%, seu produto está custando: {d2:.2f}")
elif value > 500:
    print(f"Parabéns! Você conseguiu um desconto de 30%, seu produto está custando: {d3:.2f}")
else:
    print(f"Você não obteve nenhum desconto! Você deve pagar: {value}")
