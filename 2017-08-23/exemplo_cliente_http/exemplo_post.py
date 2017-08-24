import requests

resposta = requests.post('http://127.0.0.1:8000/exemplo_post?parametro_get=valorget',
                         data={'parametro_post': 'valor do post'})

print(resposta.text)
