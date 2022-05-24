morangos = int(input('Digite a quantidade de morangos [kg]: '))
macas = int(input('Digite a quantidade de maças [kg]: '))
precoM1 = morangos * 2.50
precoM2 = morangos * 2.20

precoMc1 = macas * 1.80
precoMc2 = macas * 1.50

print('quantidade de maçãs: ', macas, '\nQuantidade de morangos: ', morangos)

if morangos > 5:
    precoFinalMorango = precoM1
else:
    precoFinalMorango = precoM2

if macas > 5:
    precoFinalMaca = precoMc1
else:
    precoFinalMaca = precoMc2

precoT = precoFinalMaca + precoFinalMorango

if precoT > 25 or (macas + morangos) > 8:
    print('Preço final: ', (precoT * 0.90))
else:
    print('Preço final: ', precoT)

