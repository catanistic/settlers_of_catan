from catan.action.base import Action, ActionFactory


class EndGame(Action):
    def __init__(self, agent, next_state, ranking):
        super().__init__(agent, next_state)
        self.ranking = ranking

    def observation(self, spectator=None):
        return self.schema(
            agent_id=self.agent.id,
        )

    def __str__(self):
        return "{} ended game with rank {}".format(
            self.agent.agent_name,
            self.ranking,
        )

    def __call__(self, game):
        game.state = self.next_state


class EndGameFactory(ActionFactory):
    def __init__(self, game, agent, next_state):
        super().__init__(game, agent, next_state)

    def __call__(self):
        """Returns a list of available actions of type action_type for the player.

        Returns:
            List of legal action of type action_type.
        """
        return [EndGame(self.agent, self.next_state, 0)]