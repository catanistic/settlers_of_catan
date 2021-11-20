from catan.action.base import ActionType, Action, ActionFactory


class Spectate(Action):
    action_type = ActionType.Spectate

    def __init__(self, spectator_id, next_state, action):
        super().__init__(spectator_id, next_state)
        self.action = action

    def observation(self, spectator_id=None):
        return self.action.__class__, self.action.observation(spectator_id)

    def __str__(self):
        return "{} watched as {}".format(
            self.agent_id.split(".")[-1],
            str(self.action), 
        )

    def __call__(self, game):
        pass


class SpectateFactory(ActionFactory):
    action_type = ActionType.Spectate

    def __call__(self, spectator_id, action, next_state):
        return [Spectate(spectator_id, next_state, action)]