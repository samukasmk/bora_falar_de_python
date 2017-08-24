import requests

resposta = requests.get('http://127.0.0.1:8000/exemplo_get')

print(resposta.text)
