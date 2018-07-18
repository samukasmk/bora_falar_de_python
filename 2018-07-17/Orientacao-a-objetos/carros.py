import os
import time

class Carro():
    
    def __init__(self, marca, velocidade_de_aceleracao = 3):
        self.marca = marca
        self.velocidade_de_aceleracao = velocidade_de_aceleracao
        self.esta_ligado = False
        self.velocidade_atual = 0
        
        
    def ligar(self):
        self.esta_ligado = True
        
    def acelerar(self):
        self.velocidade_atual += self.velocidade_de_aceleracao
        
        
meu_fusquinha = Carro(marca='fusca')
minha_ferrari = Carro(marca='ferrari', velocidade_de_aceleracao=10)

meu_fusquinha.ligar()
minha_ferrari.ligar()

voltas = 0
while voltas < 10:
    voltas += 1
    os.system("clear")
    
    meu_fusquinha.acelerar()
    minha_ferrari.acelerar()
    
    
    print("Fusca:", "#" * meu_fusquinha.velocidade_atual)
    print("Ferrari:", "#" * minha_ferrari.velocidade_atual)
    
    time.sleep(1)
    
    
    
    
    
    
    