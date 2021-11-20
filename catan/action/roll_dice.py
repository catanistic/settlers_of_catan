from catan.action.base import ActionType, Action, ActionFactory

import numpy as np


class RollDice(Action):
    action_type = ActionType.RollDice 

    def __init__(self, agent_id, next_state):
        super().__init__(agent_id, next_state)
        self.roll = np.random.randint(1, 7, 2).sum()

    def observation(self, spectator_id=None):
        raise NotImplementedError()

    def __str__(self):
        return "{} rolled {}.".format(self.agent_id.split(".")[-1], self.roll)

    def __call__(self, game):
        raise NotImplementedError()


class RollDiceFactory(ActionFactory):
    action_type = ActionType.RollDice 

    def __call__(self, game, agent_id):
        raise NotImplementedError()