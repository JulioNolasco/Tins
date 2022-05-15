import random

def embaralhar(palavra):
    return random.sample(palavra, len(palavra)) 

palavra = input("Entre com uma palavra: ")
print(palavra, "->", embaralhar(palavra))