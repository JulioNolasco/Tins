saque = int(input('Entre com o valor para sacar: '))

cem = int(saque / 100)
saque = saque - (cem*100)

cinquenta = int(saque/50)
saque = saque - (cinquenta*50)

dez = int(saque/10)
saque = saque - (dez*10)

cinco = int(saque/5)
saque = saque - (cinco*5)

um = saque

print('Notas R$100,00 = ',cem)
print('Notas R$ 50,00 = ',cinquenta)
print('Notas R$ 10,00 = ',dez)
print('Notas R$  5,00 = ',cinco)
print('Notas R$  1,00 = ',um)