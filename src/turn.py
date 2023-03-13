from src.board import Board
from src.index import store
from src.player import Player

class Turn:
    def __init__(self, square, player):
        self.square = square
        self.letter = player.letter
        self.turn_number = len(store['turns'])+1
        self.player_id = player.id
        store['turns'].append(self)
        