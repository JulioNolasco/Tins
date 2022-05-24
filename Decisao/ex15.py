a = float(input('Entre com o primeiro lado do triangulo: '))
b = float(input('Entre com o segundo lado do triangulo: '))
c = float(input('Entre com o terceiro lado do triangulo: '))

if (a + b < c) or (a + c < b) or (b + c < a):
    print('Nao é um triangulo')
elif (a == b) and (a == c) :
    print('Equilatero')
elif (a==b) or (a==c) or (b==c):
    print('Isósceles')
else:
    print('Escaleno')

