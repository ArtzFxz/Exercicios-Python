ladoRetangulo = float(input('Digite o lado do Retângulo:'))
baseRetangulo = float(input('Digite a base do Retângulo:'))
unidadeMedida = str(input('Digite a Unidade de medida dos valores: (pl)'))

somaDosLados = ladoRetangulo + ladoRetangulo + baseRetangulo + baseRetangulo
resultPerimetro = somaDosLados
resultArea = ladoRetangulo * baseRetangulo

print(f'O perímetro de seu Retângulo é {resultPerimetro:.2f} {unidadeMedida}')
print(f'A Área de seu Retângulo é {resultArea:.2f} {unidadeMedida} cúbico')