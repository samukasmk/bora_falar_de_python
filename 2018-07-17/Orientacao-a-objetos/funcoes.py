carro_marca = None
carro_velocidade = 0

def acelera_carro(marca, velocidade):
    global carro_marca, carro_velocidade
    carro_marca = marca
    carro_velocidade = carro_velocidade + velocidade
    
def liga_carro(marca, velocidade):
    global carro_marca, carro_velocidade
    carro_marca = marca
    carro_velocidade = carro_velocidade + velocidade
    
acelera_carro("Fiat", 30)
print("marca:", carro_marca)
print("velocidade:", carro_velocidade)

acelera_carro("GM", 50)
print("marca:", carro_marca)
print("velocidade:", carro_velocidade)
