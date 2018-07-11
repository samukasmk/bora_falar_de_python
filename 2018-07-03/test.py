import unittest
from url import chama_google


class TestValidaUrl(unittest.TestCase):
    
    def test_valida_protocolos(self):
        urls = ["http://www.google.com","https://www.google.com",
                "ftp://www.google.com", "ssh://www.google.com"]
        results = ['http','https','ftp','ssh']
        
        for url, result in zip(urls, results):
            with self.subTest(url=url):
                retorno = chama_google(url)
                self.assertDictEqual(retorno, {'protocolo': result, 'host': 'www.google.com', 'error': False})
     
        
    def test_verificar_so_protocolo(self):
        # with:
        protocol = 'htt'
        # when:
        retorno = chama_google(protocol)
        # then:
        expected_result = {
            'protocolo': None,
            'host': None,
            'error': False
        }
        self.assertDictEqual(retorno, expected_result)
        
    def test_verificar_protocolo_errado(self):
        # with:
        protocol = 'htt://www.google.com'
        # when:
        retorno = chama_google(protocol)
        # then:
        expected_result = {'protocolo': None,
            'host': None,
            'error': False}
        self.assertDictEqual(retorno, expected_result)   
        
    def test_valida_host(self):
        with self.subTest('host ok'):
            retorno = chama_google("http://www.google.com")
            self.assertDictEqual(retorno, {'protocolo': 'http', 'host':'www.google.com'})
            
        with self.subTest('host not ok'):
            retorno = chama_google("http://")
            self.assertDictEqual(retorno, {'protocolo': None,
            'host': None,
            'error': False})

        with self.subTest('host with ssh'):
            retorno = chama_google("ssh://")
            self.assertDictEqual(retorno, {'protocolo': None,
            'host': None,
            'error': False})
            
        with self.subTest('host with fulano'):
            retorno = chama_google("ssh://fulano%senha@git.com/")
            self.assertEqual(retorno['host'], 'fulano%senha@git.com/')
        
if __name__ == '__main__':
    unittest.main()