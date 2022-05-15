sexo = input("Entre com seu sexo, F para femino e M para masculimo")
h = float (input("Entre com sua altura"))

if(sexo == 'M'): 
    print("Seu peso ideal e: ", (72.7*h) - 58)

elif (sexo == 'F'): 
    print("Seu peso ideal e: ", (62.1*h) - 44.7)

else: print("sexo informado incorretamente!")