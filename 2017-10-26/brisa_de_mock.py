import requests
from collections import Counter

def minha_funcao():
    site_do_uol = requests.get('http://uol.com.br')
    return site_do_uol




class MockedRequests():
    cotador = Counter()
    
    def get(*args, **kwargs):
        cotador['get'] += 1
        
        if cotador['get'] > 2:
            raise DaErroAqui()
            
            