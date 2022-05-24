resultado = 'Aprovado!'

nota1=float(input('Entre com sua primeira nota: '))
nota2=float(input('Entre com sua segunda nota: '))
media=(nota1+nota2)/2
if media >=9 and media <= 10:
   conceito = 'A'
elif media >= 7.5:
   conceito = 'B'
elif media >= 6:
    conceito = 'C'
elif media >= 4:
    conceito = 'D'
elif media >= 0:
    conceito = 'E'

if media < 6:
    resultado = 'Reprovado'

print(f'Nota 1: {nota1:.2f}\nNota 2: {nota2:.2f}')
print(f'Média: {media:.2f}')
print(f'Conceito: {conceito}')
print(f'Resultado: {resultado}')
