from enum import Enum


class GameStateType(Enum):
    Default = "default"
    DevelopmentCard = "development_card"
    Robber = "robber"
    DomesticTrade = "domestic_trade"
    InitialSelection = "initial_selection"


class GameState():
    game_state = GameStateType.Default

    def __init__(self, previous_state, game):
        self.previous_state = previous_state
        self.game = game

    @property
    def action_space(self):
        """Generates the action space for the current state.

        Returns:
            A list of tuples of action and next state pairs.
        """
        pass