import math
delta = 0

for i in range(1):
    a = float(input('Entre com o valor A da equacao: '))
    if(a == 0): break
    b = float(input('Entre com o valor B da equacao: '))
    c = float(input('Entre com o valor C da equacao: '))

    delta = b*b - (4*(a*c))

    if(delta < 0): 
        print('A equacao nao possui raizes reais!')
        break
    elif(delta == 0):
        print('A equacao so tem uma raiz: ', -b/(2*a))
    else: 
        print(f'Raiz 1:{(-b + math.sqrt(delta))/(2*a):.2f}')
        print(f'Raiz 2:{(-b - math.sqrt(delta))/(2*a):.2f}')



