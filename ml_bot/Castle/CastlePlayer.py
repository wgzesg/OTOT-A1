from Castle.CastleGameContext import CastleGameContext
import numpy as np
import random
from copy import deepcopy
import math
from Castle.utils import get_input

class Player():
    def __init__(self, context: CastleGameContext, action=None, random: bool = False):
        self.game_comtext = context
        self.num_castles = context.n_castles
        self.num_soldiers = context.n_soldiers
        self.score = 0
        self.wins = []
        self.losses = []

    def get_action(self):
        pass

    def update(self, my_action, his_action, my_score):
        self.score += my_score
        if my_score < 0:
            self.losses.append((my_action, his_action, my_score))
        else:
            self.wins.append((my_action, his_action, my_score))

class CastlePlayer(Player):
    def __init__(self, gameContext: CastleGameContext, action=None, random=False):
        super().__init__(gameContext)
        self.actions = {}
        if random:
            a = self.generate_random_actions()
            self.actions[a] = 1
        elif action is not None:
            self.actions = action
            self.action_probs = [1 for i in range(len(action))]
        self.forget_bar = 100

    def __repr__(self):
        return "Player with strategy " + str(self.actions) + " winning score " + str(self.score) + " with " + str(len(self.wins)) + " wins and " + str(len(self.losses)) + " losses\n"

    def __str__(self):
        return "Player with strategy " + str(self.actions) + " winning score " + str(self.score) + " with " + str(len(self.wins)) + " wins and " + str(len(self.losses)) + " losses\n"

    def generate_random_actions(self):
        cuts = [random.randint(0, self.num_soldiers) for i in range(self.num_castles - 1)]
        cuts.append(0)
        cuts.append(self.num_soldiers)
        cuts.sort()
        actions = [cuts[i+1] - cuts[i] for i in range(self.num_castles)]
        if (sum(actions) != self.num_soldiers) or (len(actions) != self.num_castles):
            raise("Invalid action")
        return tuple(actions)

    def get_action(self) -> np.array:
        keys = list(self.actions.keys())
        cs =  random.choices(keys, weights=self.actions.values())
        return cs[0]

    def update(self, my_action: np.array, his_action: np.array, my_score: int):
        super().update(my_action, his_action, my_score)
        forgetting = False
        for action in self.actions:
            if self.actions[action] > self.forget_bar:
                forgetting = True
                self.forget_bar += 100
            p1, p2 = self.game_comtext.getPayoff(action, his_action)
            if p1 > p2:
                self.actions[action] += 1
        if forgetting:
            self.forget()
        # if len(self.actions) > 3000:
        #     self.actions = {k: v for k, v in sorted(self.actions.items(), key=lambda item: item[1], reverse=True)}
        #     self.actions = {k: v for k, v in list(self.actions.items())[:int(len(self.actions)*0.99)]}

    def forget(self):
        if len(self.actions) > 30000:
            self.actions = {k: v for k, v in sorted(self.actions.items(), key=lambda item: item[1], reverse=True)}
            self.actions = {k: v for k, v in list(self.actions.items())[:int(len(self.actions)*0.9)]}

    def mutate(self):
        new_actions = deepcopy(self.actions)
        new_actions = {k: v for k, v in sorted(new_actions.items(), key=lambda item: item[1], reverse=True)}
        for loss in self.losses:
            if loss[1] not in new_actions:
                new_actions[loss[1]] = 0
            new_actions[loss[1]] += 1
            if loss[0] in new_actions:
                new_actions[loss[0]] = 0
        if max(new_actions.values()) > 10:
            new_actions = {k: 1 for k, v in new_actions.items()}
        newPlayer = CastlePlayer(self.game_comtext, action=new_actions, random=False)
        return newPlayer

    def reset(self):
        self.score = 0
        self.wins = []
        self.losses = []
        # for k in self.actions:
        #     self.actions[k] = 1


class HumanPlayer(Player):
    def __init__(self, gameContext: CastleGameContext):
        super().__init__(gameContext)
        print("human created")

    def __repr__(self):
        return "Human player winning score " + str(self.score) + " with " + str(len(self.wins)) + " wins and " + str(len(self.losses)) + " losses\n"

    def __str__(self):
        return "Human player winning score " + str(self.score) + " with " + str(len(self.wins)) + " wins and " + str(len(self.losses)) + " losses\n"

    def get_action(self) -> np.array:
        while True:
            action = get_input()
            print("I got action " + str(action))
            if sum(action) == self.num_soldiers and len(action) == self.num_castles:
                return action
            else:
                print("Invalid action")

    def update(self, my_action: np.array, his_action: np.array, my_score: int):
        super().update(my_action, his_action, my_score)