def reverso (numero):
    return numero[::-1]

numero = input("Entre com o numero: ")
print(numero, "->", reverso(numero))