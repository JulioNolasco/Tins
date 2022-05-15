x = 0
modelo = []
consumo = []
mm = ''

for i in range(5):
    modelo.append(input("Entre com o modelo: "))
    consumo.append(float(input("Quantos Km/l ele faz: ")))


print("Comparativo de Consumo de combustivel")
for i in modelo:
    print("Veiculo: ", x+1)
    print("Nome: ", i)
    print("Km por Litro: ", consumo[x])
    x += 1
x = 0
for i in modelo:
    viagem = 1000/consumo[x]
    custo = viagem*2.25
    if(x == 0):
        menor = consumo[x]
        print("aq")
    elif(menor < consumo[x]): ##o modelo q faz mais km/l e o que menos consome
        menor = consumo[x]
        mm = i
    print("\nRelatorio Final")
    print(x+1, " - ", i, "  -      ", consumo[x], "     -     %.2f" %viagem, "Litros    -  R$ %.2f" %custo)
    x += 1

print("O menor consumo e o do: ", mm)


