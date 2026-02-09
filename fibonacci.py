n = int(input("Digite quantos termos da sequência Fibonacci: "))

firstNum = 0
secondNum = 1

print("Sequência Fibonacci:")
for i in range(n):
    print(firstNum, end=" ")
    firstNum, secondNum = secondNum, firstNum + secondNum


