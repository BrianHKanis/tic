from src.game import Game
from src.index import store

def test_game_has_id():
    game = Game()
    assert store['games'][0].id == 1
