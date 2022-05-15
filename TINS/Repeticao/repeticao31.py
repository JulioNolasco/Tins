while 1:
    x = 0
    valorTotal = 0
    mercadoria  = [float(input("Entre com o valor do produto: "))]

    while mercadoria [x] != 0:
        x += 1
        mercadoria.append(float(input("Entre com o valor do produto: ")))

    valorTotal = sum(mercadoria)
    print("Valor total: ", valorTotal)
    dinheiro = float(input("Valor em dinheiro q o cliente foreceu: "))

    for i in range (len(mercadoria)):
        print("Produto ", i, "R$", mercadoria[i])
    
    print("total: ", valorTotal)
    print("Dinheiro: ", dinheiro)
    print("Troco ", dinheiro - valorTotal)
    