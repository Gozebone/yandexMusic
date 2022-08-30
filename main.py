from current_track import current_track
from oauth import bot_token_auth


if __name__ == '__main__':
    bot = bot_token_auth()
    current_track(bot)
