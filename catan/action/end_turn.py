from catan.action.base import Action, ActionFactory


class EndTurn(Action):
    def __init__(self, agent, next_state):
        super().__init__(agent, next_state)

    def observation(self, spectator=None):
        return self.schema(
            agent_id=self.agent.id,
        )

    def __str__(self):
        return "{} ended his/her turn.".format(
            self.agent.agent_name,
        )

    def __call__(self, game):
        game.state = self.next_state


class EndTurnFactory(ActionFactory):
    def __init__(self, game, agent, next_state):
        super().__init__(game, agent, next_state)

    def __call__(self):
        """Returns a list of available actions of type action_type for the player.

        Returns:
            List of legal action of type action_type.
        """
        return [EndTurn(self.agent, self.next_state)]