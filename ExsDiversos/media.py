num1 = float(input('Digite o primeiro Número:'))
num2 = float(input('Digite o segundo Número:'))
num3 = float(input('Digite o terceiro Número:'))
num4 = float(input('Digite o quarto Número:'))

result = (num1+num2+num3+num4) / 4
resultType = float(input('Digite a média:'))

if resultType == result:
    print('Você acertou a média, parabéns')
else:
    print(f'Você errou o resultado da média desses quatro números, o resultado é {result}')