import numbers
import string


letra = input('Entre com uma letra ')

if(letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
    print('vogal')
elif(letra.isalpha()):
    print('consoante')
else:
    print('nao é uma letra!')