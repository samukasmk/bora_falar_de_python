

def jokenpo(player_1, player_2):
    if player_1 == player_2:
        return 'empate'
    
    jogadas = [player_1, player_2]
    
    if 'pedra' in jogadas and 'tesoura' in jogadas:
        return 'pedra ganha'
    
    elif 'tesoura' in jogadas and 'papel' in jogadas:
        return 'tesoura ganha'

    elif 'papel' in jogadas and 'pedra' in jogadas:
        return 'papel ganha'