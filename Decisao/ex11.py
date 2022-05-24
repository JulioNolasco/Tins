salario = float(input('Entre com o seu salario: '))  


print("Antes do reajuste: ", salario)

if salario <= 280: print("Aumento: 20%\nValor: ", salario*0.20, "\nFinal: %.2f" %(salario*1.20))
elif salario > 200 and salario <= 700: print("Aumento: 15%\nValor: ",salario*0.15 , "\nFinal: %.2f" %(salario*1.15))
elif salario > 700 and salario <= 1500: print("Aumento: 10%\nValor: ",salario*0.10 , "\nFinal: %.2f" %(salario*1.10) )
else: print("Aumento: 5%\nValor: ",salario*0.05 , "\nFinal: %.2f " %(salario*1.05))