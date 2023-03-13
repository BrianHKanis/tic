from src.index import store
from src.player import Player
import os

class Board:
    def __init__(self, player1, player2):
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ' , ' ', ' ']]
        self.player1 = player1
        self.player2 = player2
        self.id = len(store['boards'])+1
        store['boards'].append(self)
        self.turn = 1
        

    def display_board(self):
        self.turn += 1
        return print(f"""
 {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}  
---+---+---
 {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}
---+---+---
 {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}
""")
                    
    def clear_screen(self):
        return os.system('clear')

    def players(self):
        return self.player1, self.player2