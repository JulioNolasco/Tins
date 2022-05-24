numero = []
for i in range(3):
    numero.append(float(input('Entre com um numero!')))

numero.sort(reverse = True)

print('Em ordem decrescente', numero)