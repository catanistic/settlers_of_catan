from catan.action.base import ActionType, Action, ActionFactory

import numpy as np


class RollDice(Action):
    action_type = ActionType.RollDice 

    def __init__(self, agent, next_state):
        super().__init__(agent, next_state)
        self.roll = np.random.randint(1, 7, 2).sum()

    def observation(self, spectator=None):
        return self.schema(agent_id=self.agent.id)

    def __str__(self):
        return "{} rolled {}.".format(self.agent.agent_name, self.roll)

    def __call__(self, game):
        raise NotImplementedError()


class RollDiceFactory(ActionFactory):
    action_type = ActionType.RollDice 

    def __call__(self):
        """Returns a list of available actions of type action_type for the player.

        Returns:
            List of legal action of type action_type.
        """
        return [RollDice(self.agent, self.next_state)]