s = float(input("Insira o salário inícial: "))

ano = 1995
ano += 1
perc = 0.015
s += s * perc


while ano < 2007:
    ano += 1
    perc *= 2
    s += s * perc 
    print(f"Ano de {ano}, teve um aumento de {perc}, com um total de R$ {s:.2f}")