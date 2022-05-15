class BombaCombustivel:
    
    def __init__(self,  tpComb, valorLitro,  qtdComb):
        self.tpComb =  tpComb
        self.valorLitro = valorLitro
        self.qtdComb =  qtdComb

    def abastecerPorValor(self, valor):
        litroAbastecido = valor/self.valorLitro
        self.alterarQuantiidadeCombustivel(self.qtdComb - litroAbastecido)
        return litroAbastecido

    def abastecerPorLitro(self, qtd):
        vlPago = qtd * self.valorLitro
        self.alterarQuantiidadeCombustivel(self.qtdComb - qtd)
        return vlPago

    def alterarValor(self, valorLitro):
        self.valorLitro = valorLitro

    def alterarCombustivel(self, tpComb):
        self.tpComb =  tpComb

    def  alterarQuantiidadeCombustivel(self, qtdComb):
        self.qtdComb =  qtdComb


