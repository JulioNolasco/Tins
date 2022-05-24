import math

a = float(input("Altura em m: "))
litros_necessarios = a/3
no_latas = math.ceil(litros_necessarios/18)
preco_latas = no_latas*80

print('A quantidade de latas a serem compradas eh: ', no_latas)
print('O preco a ser pago sera de: ', preco_latas, 'Reais')