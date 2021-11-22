from catan.state.base import GameState, GameStateType
from catan.shared.objects import GameObjectType


class DiceRollingState(GameState):
    def __init__(self, game):
        super().__init__(game)

    @property
    def action_space(self):
        """Generates the action space for the current state.

        Returns:
            A list of actions in the current state.
        """
        pass