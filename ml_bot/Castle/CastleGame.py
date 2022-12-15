import sys
sys.path.append('Castle/')
from Game import Game
import numpy as np
from CastlePlayer import CastlePlayer
from CastleGameState import CastleGameState
import logging
log = logging.getLogger(__name__)

class CastleGame(Game):
    '''
    This class sets the rules for the Iterated Prisoners' Dilemma Game.
    '''
    def __init__(self):
        self.n_players = 2
        self.gameState = CastleGameState(np.array([1,1.5,2]))
        self.players = [CastlePlayer(self.gameState) for i in range(self.n_players)]

    def getPayoff(self):
        return self.gameState.getPayoff()

    def getGameEnded(self):
        return self.gameState.end()

    def step(self):
        actions = []
        for i in range(self.n_players):
            tempState = self.gameState.switchState(i)
            action = self.players[i].getAction(tempState)
            actions.append(action)
        self.gameState.step(actions)
    
    def getHistoryActions(self):
        return self.gameState.state
