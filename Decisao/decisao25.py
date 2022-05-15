n = 0

print("Use 'S' para sim e 'N' para nao")


pergunta = ["Telefonou para a vitima?", "Esteve no local do crime?", "Mora perto da vitima?", "Devia para a vitima?", "Ja trabalhou com a vitima?"]

for i in pergunta:
    resposta = input(i)
    if (resposta == 'S'): n += 1

if(n == 5): print("Assassino")

elif(n > 2 and n < 5 ): print("Cumplice")

elif(n == 2): print("Suspeita")

else: print("Inocente")