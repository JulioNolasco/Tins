while 1:
    saltos = []
    maior = 0
    menor = 0
    nome = input("Entre com seu nome: ")

    if(nome == ''): break
    
    for i in range(5):
        
        saltos.append(float(input("Entre com os saltos ")))

    maior = max(saltos)
    menor = min(saltos)


    print("Atleta: ", nome)
    
    for i in range(5):
        print("Salto ", i, ":", saltos[i])

    print("\nMelhor salto: ", maior)
    print("Pior salto: ", menor)

    saltos.remove(maior)
    saltos.remove(menor)
    media = sum(saltos) / len(saltos)

    print("Media dos saltos :", media, " m\n")
    print("Resultado final :")
    print(nome, ":", media, " m")
