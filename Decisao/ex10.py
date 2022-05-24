from nis import match


turno = input('Entre com o turno que voce estuda. Sendo "M"-Matutino, "V"=Vespertino e "N"-noturno: ')

if(turno == 'M'):
    print('Bom dia!')
elif(turno == 'V'):
    print('Boa tarde')
elif(turno == 'N'):
    print('Boa noite')
else: print('Valor invalido')