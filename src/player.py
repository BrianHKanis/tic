import os

print(os.getcwd())

from src.index import store
from src.game import Game

class Player:
    def __init__(self, game, letter, is_bot=False):
        self.id = len(store['players'])+1
        self.game_id = game.id
        self.letter = letter
        self.is_bot = is_bot
        store['players'].append(self)

    # Query Methods
    def turns(self):
        return [turn for turn in store['turns'] if turn.player_id == self.id]