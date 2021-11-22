from enum import Enum


class GameStateType(Enum):
    BuildingPhase = "building_phase"
    DiceRollingPhase = "roll_dice_phase"
    Setup = "setup"
    Spectate = "spectate"
    TradingPhase = "trading_phase"


class GameState():
    def __init__(self, game):
        self.game = game

    @property
    def action_space(self):
        """Generates the action space for the current state.

        Returns:
            A list of possible actions.
        """
        pass