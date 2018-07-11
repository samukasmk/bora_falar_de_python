from unittest import TestCase, main
from jokenpo import jokenpo

"""
O objetivo é fazer um juiz de Jokenpo que dada a jogada dos dois jogadores informa o resultado da partida.

As regras são as seguintes:

Pedra empata com Pedra e ganha de Tesoura
Tesoura empata com Tesoura e ganha de Papel
Papel empata com Papel e ganha de Pedra

"""

class TestJoKenPo(TestCase):
          
    def test_combinacoes(self):
        
        combinacoes = (
            # empates
            {'p1': 'pedra', 'p2': 'pedra', 'esperado': 'empate'},
            {'p1': 'tesoura', 'p2': 'tesoura', 'esperado': 'empate'},
            {'p1': 'papel', 'p2': 'papel', 'esperado': 'empate'},

            # pedra ganha
            {'p1': 'pedra', 'p2': 'tesoura', 'esperado': 'pedra ganha'},
            {'p1': 'tesoura', 'p2': 'pedra', 'esperado': 'pedra ganha'},  
           
            # tesoura ganha
            {'p1': 'tesoura', 'p2': 'papel', 'esperado': 'tesoura ganha'},
            {'p1': 'papel', 'p2': 'tesoura', 'esperado': 'tesoura ganha'},            
            
            # papel ganha
            {'p1': 'papel', 'p2': 'pedra', 'esperado': 'papel ganha'},
            {'p1': 'pedra', 'p2': 'papel', 'esperado': 'papel ganha'},
        )
            
           
        for combinacao in combinacoes:
            p1 = combinacao['p1']
            p2 = combinacao['p2']
            esperado = combinacao['esperado']
            
            with self.subTest(p1=p1, p2=p2, esperado=esperado):
                self.assertEqual(jokenpo(p1, p2), esperado)        

main()