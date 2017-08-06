import os
import getpass
import requests
from fbchat import Client
from fbchat.models import *

def give_me_an_advise(phrase):
    response = requests.post('http://text-processing.com/api/sentiment/', data={'text': phrase})
    try:
        payload = response.json()
    except:
        return 'Robo not working, heelp!'

    resp_str = payload.get('label', None)
    if resp_str == 'pos':
        return 'You are happy! jump, jump, jump, jump!'
    elif resp_str == 'neg':
        return 'Take it easy man! Why so serious ?'
    else:
        return 'Api not working, try latter'


class CustomClient(Client):
    def onMessage(self, message, author_id, thread_id, thread_type, **kwargs):
        some_adivise = give_me_an_advise(message)
        self.reply_and_speak(some_adivise, author_id)

    def reply_and_speak(self, message, author_id):
        self.sendMessage(message, thread_id=author_id, thread_type=ThreadType.USER)
        # self.speak(message)

    def speak(self, message):
        say_phrase = 'say "{}"'.format(message)
        # os.system(say_phrase)
        print(say_phrase)


if __name__ == '__main__':
    facebook_user = input('Facebook username: ')
    facebook_passwd = getpass.getpass()
    client = CustomClient(facebook_user, facebook_passwd)
    client.listen(markAlive=True)
