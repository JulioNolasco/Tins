numeroLt = float(input('Entre com a quantidade de litros vendidos: '))
tipo = input('Entre com o tipo de combustivel abastecido. Use "A" para alcool e "G" para gasolina: ')

if(tipo == 'A'):
    valor = numeroLt * 1.90
    if(numeroLt <= 20): valor *= 0.97
    else: valor *= 0.95
    print('Valor a ser pago: ', valor)
elif(tipo == 'G'):
    valor = numeroLt * 2.50
    if(numeroLt <= 20): valor *= 0.96
    else: valor *= 0.94
    print('Valor a ser pago: ', valor)
else: print('Combustivel invalido!!')