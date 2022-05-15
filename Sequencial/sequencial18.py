arq = float(input("Entre com o Tamanho do arquivo em MB: "))
vlcIn = float(input("Entre com a Velocidade de Internet em Mbps: "))

print("Tempo aproxiamdo do download: %.0f Minutos " %(60 * (arq / vlcIn)))