
Produto1 = float(input('Entre com o valor do primeiro produto: '))
Produto2 = float(input('Entre com o valor do segundo produto: '))
Produto3 = float(input('Entre com o valor do terceiro produto: '))

if Produto1 < Produto2:
    if Produto1 < Produto3:
        print('Voce deve comprar o primeiro produto!')
    else:
        print('Voce deve comprar o terceiro produto!')
else:
    if Produto2 < Produto3:
        print('Voce deve comprar o segundo produto!')
    elif(Produto3 < Produto2):
        print('Voce deve comprar o terceiro produto!')
    else: print('Os produtos sao do mesmo valor!')