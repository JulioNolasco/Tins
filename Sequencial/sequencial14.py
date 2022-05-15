peso = float(input ("Entre com o peso do peixe: "))

if(peso > 50): 
    excesso = peso - 50
    multa = excesso*4
    print("Exesso de peso: ", excesso, "Kg")
    print("Multa por exesso de peso: ", multa, "reais")

else: print("Peixe dentro do peso aceitavel pelo regulamento de pesca")

