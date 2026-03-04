nome = str(input('Digite seu nome: '))
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / altura ** 2

print(f'{nome}, seu IMC com base em seu peso e altura é {imc:.1f}')

if 18.5 <= imc <= 24.5: 
    print('Seu IMC está saudável!')
elif imc < 18.5:
    print('Seu IMC está abaixo do peso!')
else:
    print('Seu IMC está acima do peso!')
    