from catan.action.base import ActionType, Action, ActionFactory
from catan.resource import ResourceType
from catan.shared import FieldType

DEVELOPMENT_CARD_PRICE = {
    ResourceType.Wheat: 1,
    ResourceType.Ore: 1,
    ResourceType.Wool: 1,
}


class BuyDevelopmentCard(Action):
    action_type = ActionType.BuyDevelopementCard

    def __init__(self, agent, next_state):
        super().__init__(agent, next_state)
        self.price = DEVELOPMENT_CARD_PRICE

    def observation(self, spectator=None):
        return self.schema(
            agent_id=self.agent.id,
        )

    def __str__(self):
        return "{} has bought a development card".format(
            self.agent.agent_name)

    def __call__(self, game):
        self.agent.pay(self.price, game)
        game.state = self.next_state


class BuyDevelopmentCardFactory(ActionFactory):
    def __call__(self):
        """Returns a list of available actions of type action_type for the player.

        Returns:
            List of legal action of type action_type.
        """
        raise NotImplementedError()