import os
from yandex_music import Client


def OAuth():
    print(os.environ.get('TOKEN'))
    return Client(os.environ.get('TOKEN')).init()
