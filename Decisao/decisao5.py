n1 = float(input("Entre com sua primeira nota"))
n2 = float(input("Entre com sua segunda nota"))

notaF = (n1+n2)/2

if(notaF == 10.0): print("Aprovado com Distincao")

elif (notaF >= 7.0): print("Aprovado")

elif (notaF < 7.0): print("Reprovado")
