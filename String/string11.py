import random

consulta = open("palavras.txt",'r')
palavras = consulta.readlines()
consulta.close()

def print_forca(forca):
    print(' '.join(forca).upper())
    print('')
	
palavra = random.choice(palavras)

forca = ['_' for i in range(len(palavra)-1)]
erros = 0
ganhou = False


while erros < 6 and not ganhou:
    print_forca(forca)
    print('Digite uma letra:')
    chute = str(input()).lower()

    if chute not in palavra:
        erros += 1
        print(f'Você errou pela {erros} vez. Tente de novo!.')
        continue

    for index, letra in enumerate(palavra):
        if letra == chute:
            forca[index] = chute

    if '_' not in forca:
        ganhou = True

if ganhou:
    print('You win!')
else:
    print('Game over!')
print_forca(forca)