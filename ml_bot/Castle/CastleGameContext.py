import numpy as np
from typing import List

class CastleGameContext():
    def __init__(self, n_castles: int=8, n_solders: int=50, payoff: np.array = None):
        self.n_castles = n_castles
        self.n_soldiers = n_solders
        self.payoff = payoff if payoff is not None else np.array(n_castles)

    def getPayoff(self, action1: List[int], action2: List[int]):
        if sum(action1) > self.n_soldiers or sum(action2) > self.n_soldiers:
            raise("Invalid action")
        if len(action1) != self.n_castles or len(action2) != self.n_castles:
            raise("Invalid action")
        score1, score2 = 0, 0
        for a, b, val in zip(action1, action2, self.payoff):
            if a > b:
                score1 += val
            elif a < b:
                score2 += val
            else:
                score1 += val/2
                score2 += val/2
        return score1, score2

