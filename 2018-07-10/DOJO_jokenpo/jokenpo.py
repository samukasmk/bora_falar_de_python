import getpass

def jokenpo(player_1, player_2):
    if player_1 == player_2:
        return 'empate'
    
    jogadas = [player_1, player_2]
    
    if 'pedra' in jogadas and 'tesoura' in jogadas:
        jogada_ganhadora = 'pedra'
        if player_1 == jogada_ganhadora:
            player_ganhador = 'player 1'
        else:
            player_ganhador = 'player 2'
    
    elif 'tesoura' in jogadas and 'papel' in jogadas:
        jogada_ganhadora = 'tesoura'
        if player_1 == jogada_ganhadora:
            player_ganhador = 'player 1'
        else:
            player_ganhador = 'player 2'


    elif 'papel' in jogadas and 'pedra' in jogadas:
        jogada_ganhadora = 'papel'
        if player_1 == jogada_ganhadora:
            player_ganhador = 'player 1'
        else:
            player_ganhador = 'player 2'
            
    else:
        return 'digite uma opcao valida'
        
    return jogada_ganhadora + ' ganha com: ' + player_ganhador


if __name__ == '__main__':
    while True:
        p1 = getpass.getpass('[Player 1] digite sua jogada: ')
        p2 = getpass.getpass('[Player 2] digite sua jogada: ')
        resultado = jokenpo(p1, p2)
        print()
        print('player 1 jogou:', p1)
        print('player 2 jogou:', p2)
        print(resultado)
        print('---')
        
        