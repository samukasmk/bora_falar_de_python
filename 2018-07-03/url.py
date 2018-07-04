

def chama_google(url):
    url_dict = {
        'error': False,
        'protocolo': None,
        'host': None
    }
    lista_hosts = ['http', 'https', 'ssh', 'ftp']
    protocol_splited = url.split('://')
    if len(protocol_splited) <2 or protocol_splited[0] not in lista_hosts:
        url_dict['error'] = True
        return url_dict
    else:
        url_dict['protocolo'] = protocol_splited[0]
        url_dict['host'] = protocol_splited[1]
    
    if len(url_dict['host']) > 0:
        url_dict['host'] = protocol_splited[1]
    else:
        return {'error': True}
    
    return url_dict