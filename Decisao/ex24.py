n1 = float(input('Entre com o número 1: '))
n2 = float(input('Entre com o número 2: '))
operacao = input('Entre com a operação que deseja realizar: [+, -, /, *]: ')


def verifica():
    if (resultadoOp // 1 == resultadoOp):
        print('Inteiro')
        if resultadoOp % 2 == 0:
            print('Par')
        else:
            print('Impar')
    else:
        print('Decimal')
    if resultadoOp > 0:
        print('Positivo')
    else:
        print('Negativo')


if operacao == '+':
    resultadoOp = n1 + n2
    print('Resultado: ', resultadoOp)
    verifica()
elif operacao == '-':
    resultadoOp = n1 - n2
    print('Resultado: ', resultadoOp)
    verifica()
elif operacao == '/':
    resultadoOp = n1 / n2
    print('Resultado: ', resultadoOp)
    verifica()
elif operacao == '*':
    resultadoOp = n1 * n2
    print('Resultado: ', resultadoOp)
    verifica()
else:
    print('Valor Invalido')