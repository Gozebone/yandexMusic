import os
from yandex_music import Client
from token_getter import get_token


def oauth(token):
    return Client(token).init()


def new_token_auth():
    token = get_token()
    return oauth(token)


def bot_token_auth():
    token = os.environ.get('BOT_TOKEN')
    return oauth(token)
