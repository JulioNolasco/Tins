import math

a = float(input("Altura em m: "))
area_com_folga = a*1.1
litros_necessarios = area_com_folga/6
no_latas = math.ceil(litros_necessarios/18)
no_galoes = math.ceil(litros_necessarios/3.6)
preco_apenas_latas = no_latas*80
preco_apenas_galoes = no_galoes*25

print(f"Comprar {no_latas} latas, totalizando de R${preco_apenas_latas:.2f}.")

print(f"Comprar {no_galoes} galões, totalizando de R${preco_apenas_galoes:.2f}.")

no_latas = math.floor(litros_necessarios/18)
preco_de_latas = no_latas*80
litros_faltantes = litros_necessarios % 18
no_galoes = math.ceil(litros_faltantes/3.6)
preco_de_galoes = no_galoes*25

if litros_faltantes <= 10.8:
    print(f"Comprar {no_latas} latas e {no_galoes} galões, totalizando R${preco_de_latas + preco_de_galoes:.2f}.")