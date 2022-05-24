n1 = float(input('Entre com sua primeira nota: '))
n2 = float(input('Entre com sua segunda nota: '))

nota = (n1 + n2) / 2

if(nota == 10):     
    print ('Aprovado com distinção !!')
elif(nota >= 7 and nota < 10):
    print ('Aprovado')    
else:
    print ('Reprovado')