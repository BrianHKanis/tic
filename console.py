from src.game import Game
from src.player import Player
from src.board import Board
from src.turn import Turn
from src.square import Square
from src.index import store
from src.services.play_game import *

print_welcome()
game = Game()
while True:
    player1, player2, board = initialize_players_and_board(game)
    current_board = True
    while current_board:
        x, y, letter, current_player, other_player = player_turn(board)
        validate_input(board, x, y, letter)
        board.clear_screen()
        board.display_board()
        if check_status(board) == 1:
            store["game_score"]["wins"].append(current_player.letter)
            print(f"The winner is {current_player.letter}")
            current_board = False
        elif check_status(board) == 2:
            print("It's a tie!")
            store["game_score"]["ties"] += 1
            current_board = False
    game.display_score(store)
    if play_again() == 1:
        continue
    else:
        break