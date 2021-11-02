from enum import Enum


class GameStateType(Enum):
    BuildingPhase = "building_phase"
    DevelopmentCard = "development_card"
    DiceRollingPhase = "roll_dice_phase"
    Robber = "robber"
    Setup = "setup"
    Spectate = "spectate"
    TradingPhase = "trading_phase"


class GameState():
    game_state = None

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