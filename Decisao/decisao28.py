precoAL = 5.90
precoFile = 4.90
precopican = 6.90
acrescimo = 0.90
desconto = 0.0

print("1) File Duplo")
print("2) Alcatra")
print("3) Picanha")

tipo = int(input("Qual o tipo da carne? "))
kg = int(input("Quantos quilos ira levar? "))

if(kg > 5):
    precoFile += acrescimo
    precoAL += acrescimo
    precopican += acrescimo

if(tipo == 1): 
    precoFinal = kg*precoFile
    tipo = "File Duplo"

elif(tipo == 2): 
    precoFinal = kg*precoAL
    tipo = "Alcatra"

elif(tipo == 3): 
    precoFinal = kg*precopican
    tipo = "Picanha"

else: print("Opcao invalida!!")

cartao = input("Ira pagar com o cartao tabajara? 'S' pra sim 'N' pra nao")

if(cartao == 'S'):
    tipoPag = "Cartao tabajara"
    desconto = precoFinal*0.05
else:
    tipoPag = input("Qual tipo de pagamento? ")

print("Tipo da carne: ", tipo)
print(kg, "kg de carne")
print("Preco final: ", precoFinal)
print("tipo de pagamento: ", tipoPag)
print("Valor do desconto: ", desconto)
print("Valor a pagar: ", precoFinal - desconto)