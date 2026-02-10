nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"O Aluno foi aprovado! Média: {media}")
else:
    print(f"O Aluno foi reprovado! Média: {media}")