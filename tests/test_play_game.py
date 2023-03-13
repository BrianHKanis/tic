from src.services.play_game import *
from src.player import *
from src.turn import *
from src.game import *
from src.board import *

def test_player_input():
    game = Game()
    player1 = Player(game, 'X')
    player2 = Player(game, 'O')
    board = Board(player1, player2)
    player_input(board, 1, 1, 'X')
    assert board.board[1-1][1-1] == 'X'

def test_validate_input():
    game = Game()
    player1 = Player(game, 'X')
    player2 = Player(game, 'O')
    board = Board(player1, player2)
    x = 1
    y = 1
    letter = player1.letter
    assert validate_input(board, x, y, letter) == None

def test_check_row_status():
    game = Game()
    player1 = Player(game, 'X')
    player2 = Player(game, 'O')
    board = Board(player1, player2)
    board.board[0] = ['X', 'X', 'X']
    assert check_row_status(board) == 1

def test_check_column_status():
    game = Game()
    player1 = Player(game, 'X')
    player2 = Player(game, 'O')
    board = Board(player1, player2)
    for i in range(0, 3, 1):
        board.board[i][0] = 'X'
    assert check_column_status(board) == 2

def test_check_diagonal_status():
    game = Game()
    player1 = Player(game, 'X')
    player2 = Player(game, 'O')
    board = Board(player1, player2)
    for i in range(0, 3, 1):
        board.board[i][i] = 'X'
    assert check_diagonal_status(board) == 3

def test_check_tie_status():
    game = Game()
    player1 = Player(game, 'X')
    player2 = Player(game, 'O')
    board = Board(player1, player2)
    for i in range(0, 3, 1):
        board.board[i] = ['X', 'X', 'X']
    assert check_tie_status(board) == 4
