class Humano:
    def __init__(self, cor_dos_olhos, altura, peso):
        self.cor_dos_olhos = cor_dos_olhos
        self.altura = altura
        self.peso = peso
        self.idade = 0
        
    def hoje(self):
        print("Cor dos olhos: ", self.cor_dos_olhos)
        print("Altura: ", self.altura)
        print("Peso: ", self.peso)
        print("Idade: ", self.idade)
        
    def mais_dez_anos(self):
        self.altura += 1.0
        self.peso += 30
        self.idade += 10
        
samuka = Humano(cor_dos_olhos='castanho', altura=0.30, peso=12)
samuka.hoje()
samuka.mais_dez_anos()
samuka.hoje()