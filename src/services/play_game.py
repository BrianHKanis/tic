from src.game import Game
from src.player import Player
from src.board import Board
from src.turn import Turn
from src.square import Square

def print_welcome():
    print("Welcome to the game of Tic-Tac-Toe")
    print()
    print("The board consists of the following coordinates:")
    print(("""
     1 | 2 | 3  
    ---+---+---
     4 | 5 | 6
    ---+---+---
     7 | 8 | 9
    """))

def initialize_players_and_board(game):
    player1_char = input("Player 1, please choose your character: ")
    player2_char = input("Player 2, please choose your character: ")
    player1 = Player(game, player1_char)
    player2 = Player(game, player2_char)
    board = Board(player1, player2)
    return player1, player2, board

def prompt(board):
    if board.turn % 2 != 0:
        current_player = board.player1
        other_player = board.player2
    else:
        current_player = board.player2 
        other_player = board.player1
    letter = current_player.letter
    print(f"'{letter}' it's your turn")
    square_number = int(input("Square Number: "))
    return square_number, letter, current_player, other_player

def player_turn(board):
    square_number, letter, current_player, other_player = prompt(board)
    square = Square(square_number, letter)
    Turn(square, current_player)
    x = square.square_to_x()
    y = square.square_to_y()
    return x, y, letter, current_player, other_player

def player_input(board, x, y, letter):
    if board.board[x-1][y-1] != ' ':
        return 0
    else:
        board.board[x-1][y-1] = letter
        return 1

def validate_input(board, x, y, letter):
    while player_input(board, x, y, letter) == 0:
        print("This square is occupied. Please try again.")
        x, y, letter, current_player, other_player = player_turn(board)
        if player_input(board, x, y, letter) == 1:
            break


def check_row_status(board):
    if len(set(board.board[0])) == 1 and board.board[0][0] != ' ':
        return 1
    if len(set(board.board[1])) == 1 and board.board[1][0] != ' ':
        return 1
    if len(set(board.board[2])) == 1 and board.board[2][0] != ' ':
        return 1
    
def check_column_status(board):
    if board.board[0][0] == board.board[1][0] == board.board[2][0] and board.board[0][0] != ' ':
        return 2
    if board.board[0][1] == board.board[1][1] == board.board[2][1] and board.board[0][1] != ' ':
        return 2
    if board.board[0][2] == board.board[1][2] == board.board[2][2] and board.board[0][2] != ' ':
        return 2
        
def check_diagonal_status(board):
    if board.board[0][0] == board.board[1][1] == board.board[2][2] and board.board[0][0] != ' ': 
        return 3
    if board.board[0][2] == board.board[1][1] == board.board[2][0] and board.board[0][2] != ' ':
        return 3


def check_tie_status(board):
    if board.board[0].count(' ') == 0 and board.board[1].count(' ') == 0 and board.board[2].count(' ') == 0:
        return 4

def check_status(board):
    if check_row_status(board) or check_column_status(board) or check_diagonal_status(board):
        return 1
    if check_tie_status(board):
        return 2
    
def play_again():
    print("Would you like to play again?")
    answer = input("(y)es or (n)o: ")
    if answer == 'y' or answer == 'Y':
        return 1