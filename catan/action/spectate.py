from catan.action.base import ActionType, Action, ActionFactory


class Spectate(Action):
    action_type = ActionType.Spectate

    def __init__(self, spectator, next_state, action):
        super().__init__(spectator, next_state)
        self.action = action

    def observation(self, spectator=None):
        return self.action.__class__, self.action.observation(self.agent)

    def __str__(self):
        return "{} watched as {}".format(
            self.agent.agent_name,
            str(self.action), 
        )

    def __call__(self, game):
        pass


class SpectateFactory(ActionFactory):
    action_type = ActionType.Spectate

    def __call__(self, spectator, action, next_state):
        return [Spectate(spectator, next_state, action)]