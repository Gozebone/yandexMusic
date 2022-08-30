import os
from yandex_music import Client
from tokenGetter import getToken


def OAuth():
    token = getToken()
    print(token)
    print(os.environ.get('TOKEN'))
    return Client(token).init()
