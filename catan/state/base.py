from enum import Enum


class GameStateType(Enum):
    Default = "default"
    Monopoly = "monopoly"
    MovingRobber = "robber_move"
    RoadBuilding = "road_building"
    Robbing = "robbing"
    Start = "start_of_game"
    TurnAfterDice = "after_dice"
    TurnBeforeDice = "before_dice"
    YearOfPlenty = "year_of_plenty"


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