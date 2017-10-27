import json
import requests

from requests.exceptions import BaseHTTPError
from unittest import TestCase, main
from unittest.mock import MagicMock, patch, create_autospec

import ultimos_lancamentos
from ultimos_lancamentos import (qual_foi_o_ultimo, 
                                 qual_foi_o_penultimo,
                                 pega_lancamento,
                                 pega_todos_lancamentos_fake,
                                 pega_todos_lancamentos_validos,
                                 LINK_API)


with open('data.json') as data_file:    
    retorno_da_api_spacex = json.load(data_file)

class MockedGet():
    def __init__(self, *args, **kwargs):
        pass
    
    def json():
        return retorno_da_api_spacex

class TestUltimosLancamentos(TestCase):
    

    def setUp(self):
        pass
    
    
    def test_de_uma_substituicao_da_chamada_requests_get_por_meu_resultado_fake(self):    
        class Requests():
            pass
        
        requests = Requests()
 
        requests.get = MagicMock(return_value=retorno_da_api_spacex)
        
        resultado = requests.get('x')
        
        self.assertEqual(resultado[0]['flight_number'], 1)
        
    
    def test_tem_link(self):
        self.assertEqual(LINK_API,'mexi aqui para nao pegar da internet')
    
  
    def test_ultimo_lancamento(self):        
        with patch.object(ultimos_lancamentos, 'get', return_value=MockedGet) as mock_method:
            lancamento = qual_foi_o_ultimo()
        
        self.assertEqual(lancamento['flight_number'], 49)
        
    def test_penultimo_lancament(self):
        mock_qual_foi_o_penultimo = create_autospec(qual_foi_o_penultimo, return_value=retorno_da_api_spacex[47])
        lancamento = mock_qual_foi_o_penultimo()

        self.assertEqual(lancamento['flight_number'], 48)
        
    def test_pega_lancamento_42(self):
        lancamento = pega_lancamento(42)
        
        self.assertEqual(lancamento['flight_number'], 42)

    def test_pega_lancamento_45(self):
        lancamento = pega_lancamento(45)
        
        self.assertEqual(lancamento['flight_number'], 45)

    def test_ano_ultimo_lancamento(self):
        lancamento = pega_lancamento(49)
        
        self.assertEqual(lancamento['launch_year'], '2017')
        
    def test_pega_todos_lancamentos_fake(self):
        lancamentos = pega_todos_lancamentos_fake()
        
        self.assertEqual(len(lancamentos),49)
    
    def test_checa_numero_lancamentos_maior_que_1(self):
        lancamentos = pega_todos_lancamentos_validos()
        
        self.assertGreater(len(lancamentos), 1)
    
    def test_checa_se_o_primeiro_lancamento_veio_com_id_igual_1(self):
        lancamentos = pega_todos_lancamentos_validos()
     
        self.assertEqual(lancamentos[0]['flight_number'], 1)
    
    def test_se_o_primeiro_elemento_eh_um_dicionario(self):
        lancamentos = pega_todos_lancamentos_validos()
        
        for i, valor_do_lancamento in enumerate(lancamentos):
            self.assertIsInstance(lancamentos[i], dict)
            
        
if __name__ == '__main__':
    main()