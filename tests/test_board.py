from src.game import Game
from src.player import Player
from src.board import Board
from src.index import store

def test_board_has_id():
    game = Game()
    player1 = Player(game, 'X')
    player2 = Player(game, 'O')
    board = Board(player1, player2)
    assert store['boards'][-1] == board 

def test_board_has_2_players():
    game = Game()
    player1 = Player(game, 'X')
    player2 = Player(game, 'O')
    board = Board(player1, player2)
    assert len(board.players()) == 2