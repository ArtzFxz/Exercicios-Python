# EXERCICIO FIXACAO LISTA 4 - PRIME BOT -- Robô-analista para tirar a StartUp TechInvest da Crise!

print("=== PRIME - Seu Primeiro Robô Analista ===")
# Fase 1
nome = input("Qual é o seu nome? ")
renda = float(input("Qual é a sua renda mensal? R$ "))
gasto = float(input("Qual é o seu gasto mensal? R$ "))
coragem = int(input("Qual seu nível de coragem para investir? (1 a 10) "))

# Fase 2
print("\n=== DIAGNÓSTICO FINANCEIRO ===")

if gasto > renda:
    print("Emergência Financeira! Seus gastos são maiores que sua renda.")
else:
    sobra = renda - gasto
    reservaNecessaria = gasto * 6
    print(f"Você tem R$ {sobra:.2f} sobrando por mês.")

    if sobra >= reservaNecessaria:
        print("Parabéns! Você já consegue montar sua reserva de segurança.")
    else:
        falta = reservaNecessaria - sobra
        print(f"Para formar sua reserva de segurança (6x gasto mensal), faltam R$ {falta:.2f}.")

#Fase 3
print("\n=== ARVORE DE DECISAO ===")

if coragem < 4:
    perfil = "Tesouro Direto"
elif 4 <= coragem <= 7:
    perfil = "Fundos Imobiliários"
else:
    perfil = "Ações de Tecnologia"

print(f"Com seu nível de coragem {coragem}, sua melhor estratégia inicial seria: {perfil}")

#Fase 4
print("\n=== MAQUINA DO TEMPO ===")

anos = int(input("\nQuantos anos você pretende investir? "))

if gasto <= renda:
    patrimonio = 0
    aporte_anual = (renda - gasto) * 12
    
    for ano in range(1, anos + 1):
        patrimonio += aporte_anual
    
    print(f"\nSe você investir com disciplina por {anos} anos, poderá acumular aproximadamente R$ {patrimonio:.2f} (sem considerar juros).")

print("\n=== Obrigado por usar o PRIME - TechInvest ===")