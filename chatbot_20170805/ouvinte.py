import os
import getpass
from fbchat import Client
from fbchat.models import *

class CustomClient(Client):
    def onMessage(self, message, author_id, thread_id, thread_type, **kwargs):
        # Do something with the message here
        frase_para_dizer = 'say "{}"'.format(message)
        os.system(frase_para_dizer)


if __name__ == '__main__':
    facebook_user = input('Facebook username: ')
    facebook_passwd = getpass.getpass()
    client = CustomClient(facebook_user, facebook_passwd)
    client.listen(markAlive=True)
