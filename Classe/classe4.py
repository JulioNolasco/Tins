class Pessoa:
    
    def __init__ (self,nome,peso,altura,idade):
        self.idade = int(idade)
        self.nome = nome
        self.peso = float(peso)
        self.altura = float(altura)

    def envelhecer (self,anos):
        if self.idade < 21:
            self.altura += 0.05
        self.idade += anos

    def engordar (self,kg):
        self.peso += kg

    def emagrecer (self,kg):
        self.peso -= kg

    def crescer (self,cm):
        self.altura += cm