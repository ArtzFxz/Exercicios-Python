p1  = input("Você telefonou para a vítima? (Sim/Não)")
p2  = input("Esteve no local do crime? (Sim/Não)")
p3  = input("Mora perto da vítima? (Sim/Não)")
p4  = input("Você devia para a vítima? (Sim/Não)")
p5  = input("Já trabalhou com a vítima? (Sim/Não)")

respostas = 0


if p1 == "Sim":
    respostas += 1

if p2 == "Sim":
    respostas += 1

if p3 == "Sim":
    respostas += 1

if p4 == "Sim":
    respostas += 1

if p5 == "Sim":
    respostas += 1


if respostas <= 1:
    print("Inocente!")
elif respostas == 2:
    print("Suspeito!")
elif 3 <= respostas <= 4:
    print("Cúmplice!")
else:
    print("ASSASSINO!")