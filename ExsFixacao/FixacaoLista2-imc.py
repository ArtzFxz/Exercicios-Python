# EXERCICIO FIXACAO LISTA 2 - IMC

Inome = str(input('Digite seu nome: '))
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / altura ** 2

print(f'{Inome}, seu IMC com base em seu peso e altura é {imc:.1f}')

if 18.5 <= imc <= 24.5: 
    print('Seu IMC está saudável! (normal)')
elif imc < 18.5:
    print('Seu IMC está abaixo do peso!')
elif 25.0 == imc <= 29.9:
    print('Seu IMC está sobrepeso!')
else:
    print("Obesidade!")