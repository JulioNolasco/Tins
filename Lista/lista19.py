ws = 0
un = 0
lx = 0
nt = 0
mo = 0
ot = 0
total = 0
op = 1

while op != 0:
    print("Qual o melhor Sistema Operacional para uso em servidores?\n")
    print("1 - Windows Server ")
    print("2 - Unix ")
    print("3 - Linux ")
    print("4 - Netawre ")
    print("5 - Mac OS ")
    print("6 - Outro ")

    op = int(input("Escolha uma opcao: "))

    match op:
        case 1:
            ws += 1
        case 2:
            un += 1
        case 3:
            lx += 1
        case 4:
            nt += 1
        case 5:
            mo += 1
        case 6:
            ot += 1
sos = [ws, un, lx, nt, mo, ot]
    
total = (ws + un + lx + nt + mo + ot)
print("Sistema Operacional       Votos    %")
print("-------------------       -----   ---\n")
print("Windows Server             ", ws,"    ", "%.2f" %((ws*100)/total),end = "%")
print("Unix                       ", un,"    ", "%.2f" %((un*100)/total),end = "%")
print("Linux                      ", lx,"    ", "%.2f" %((lx*100)/total),end = "%")
print("Netware                    ", nt,"    ", "%.2f" %((nt*100)/total),end = "%")
print("Mac OS                     ", mo,"    ", "%.2f" %((mo*100)/total),end = "%")
print("Outro                      ", ot,"    ", "%.2f" %((ot*100)/total),end = "%")
print("O Sistema Operacional mais votado foi o ", max(sos), "com ",max(sos)," votos, correspondendo a 40% dos votos.")

        