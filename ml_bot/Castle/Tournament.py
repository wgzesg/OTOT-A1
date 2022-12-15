from Castle.CastlePlayer import CastlePlayer
from Castle.CastleGameContext import CastleGameContext
import pickle

class Tournament():
    def __init__(self, pool_size, game_context: CastleGameContext, fill_random=True):
        self.pool_size = pool_size
        self.game_context = game_context
        self.players = []
        if fill_random:
            self.fill_random()

    def fill_random(self):
        while (len(self.players) < self.pool_size):
            self.players.append(CastlePlayer(self.game_context, random=True))
    
    def add_player(self, player):
        self.players.append(player)

    def run_tournament(self, reps=1, verbose=False):
        for i in range(len(self.players)):
            for j in range(i+1, len(self.players)):
                self.play_match(self.players[i], self.players[j], reps, verbose)
        self.players.sort(key=lambda x: len(x.wins), reverse=True)

    def set_players(self, players):
        self.players = players
        self.reset()

    def reset(self):
        for p in self.players:
            p.reset()

    def get_best_player(self):
        return self.players[0]
    
    def get_all_players(self):
        return self.players

    def play_match(self, player1, player2, reps=1, verbose=False):
        for i in range(reps):
            action1 = player1.get_action()
            action2 = player2.get_action()
            score1, score2 = self.game_context.getPayoff(action1, action2)
            player1.update(action1, action2, score1 - score2)
            player2.update(action2, action1, score2 - score1)
            if verbose:
                print("Player1: " + str(action1) + " Player2: " + str(action2) + " Score1: " + str(score1) + " Score2: " + str(score2))
    
    def save(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, f)