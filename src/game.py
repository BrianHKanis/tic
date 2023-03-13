from src.index import store

class Game:
    def __init__(self):
        self.id = len(store['games']) + 1
        store['games'].append(self)

    def display_score(self, store):
        return print(f"Wins: {store['game_score']['wins']}    Losses: {store['game_score']['losses']}    Ties: {store['game_score']['ties']}")