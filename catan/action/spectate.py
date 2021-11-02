from catan.action.base import ActionType, Action, ActionFactory


class Spectate(Action):
    action_type = ActionType.EarnResource

    def __init__(self, agent_id, next_state, action):
        super().__init__(agent_id, next_state)
        self.action = action

    def observation(self, spectator_id=None):
        raise NotImplementedError()

    def __str__(self):
        return "{} watched as {}".format(
            self.agent_id.split(".")[-1],
            str(self.action), 
        )

    def __call__(self, game):
        raise NotImplementedError()


class SpectateFactory(ActionFactory):
    action_type = ActionType.Spectate

    def action_space(self, game, agent_id):
        raise NotImplementedError()