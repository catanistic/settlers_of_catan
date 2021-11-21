from catan.action.spectate import SpectateFactory
from catan.state.base import GameState, GameStateType
from catan.shared.objects import GameObjectType


class SpectateGameState(GameState):
    game_state = GameStateType.Spectate

    def __init__(self, game, action):
        """
            Args:
                game: Game object.
                spectator_ids: list of Agent ids that spectate the action.
                next_state: the State that comes after spectation.
                action: the action that will be executed.
        """
        super().__init__(game)
        self.curr_spectator = 0
        self.next_state = action.next_state
        self.specator_ids = list(game.ids[GameObjectType.Agent])
        self.specator_ids = filter(lambda x: x != action.agent.id, self.specator_ids)
        self.action = action
        self.actionFactory = SpectateFactory()

    @property
    def action_space(self):
        """Generates the action space for the current state.

        Returns:
            A list of tuples of action and next state pairs.
        """
        if self.curr_spectator < len(self.specator_ids):
            spectator_id = self.spectator_ids[self.curr_spectator]
            spectator = self.game.game_objects[spectator_id]
            self.curr_spectator += 1
            return self.actionFactory.action_space(spectator, self.action, self)
        return [self.action]