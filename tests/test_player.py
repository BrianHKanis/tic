from src.player import *
from src.turn import *
from src.game import *
from src.square import *

def test_player_is_added_to_store():
    game = Game()
    letter = 'X'
    player = Player(game, letter)
    assert store['players'][-1] == player

def test_player_has_id():
    game = Game()
    letter = 'X'
    player = Player(game, letter)
    test_player = store['players'][-1]
    assert test_player.letter == 'X'

def test_turns():
    game = Game()
    letter = 'X'
    player = Player(game, letter)
    square = Square(1, letter)
    turn = Turn(square, player)
    assert player.turns() == [turn]