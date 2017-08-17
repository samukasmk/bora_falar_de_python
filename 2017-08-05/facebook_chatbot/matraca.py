#!/usr/bin/python
import getpass
from fbchat import Client
from fbchat.models import *

facebook_user = input('Facebook username: ')
facebook_passwd = getpass.getpass()
contant_name = input('Facebook contact name to send messages: ')

client = CustomClient(facebook_user, facebook_passwd)

usuarios = cliente.searchForUsers(contant_name)
samuka = usuarios[0]

for valor_diferente_em_cada_vez in range(1, 51):
    mensagem = str(valor_diferente_em_cada_vez) + ' elefante incomoda muita gente'
    cliente.sendMessage(mensagem, thread_id=samuka.uid, thread_type=ThreadType.USER)
