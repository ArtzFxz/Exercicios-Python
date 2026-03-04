# EXERCICIO FIXACAO LISTA 2 - IS

dados_originais = [10, 20, 30]
dados_referencia = dados_originais
dados_copia = [10, 20, 30]

if dados_referencia is dados_originais:
    print(dados_referencia is dados_originais)
else:
    print("False")
if dados_copia is dados_originais:
    print(dados_copia is dados_originais)
else:
    print("False")