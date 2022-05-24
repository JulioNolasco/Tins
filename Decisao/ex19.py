for i in range(1):
    plural = ''

    numero = int(input('Entre com um numero inteiro menor q 1000: '))
    if(numero >= 1000): break
    centena = numero // 100
    dezena = (numero - (centena*100)) // 10
    unidade = numero - ((centena*100)+dezena*10)
    
    print(centena,'centena(s),',dezena,'dezena(s) e',unidade,'unidade(s)')