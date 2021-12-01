from catan.action.base import ActionType, Action, ActionFactory
from catan.resource import ResourceType
from catan.shared import FieldType 


CITY_PRICE = {
    ResourceType.Clay: 1,
    ResourceType.Wheat: 1,
    ResourceType.Wood: 1,
    ResourceType.Wool: 1,
}


class UpgradeSettlement(Action):
    action_type = ActionType.UpgradeSettlement

    def __init__(self, agent, next_state, node):
        super().__init__(agent, next_state)
        self.node = node 
        self.schema.append_field("node_id", FieldType.GameObjectReference)

    def observation(self, spectator=None):
        return self.schema(
            agent_id=self.agent.id,
            node_id=self.node.id,
        )

    def __str__(self):
        return "{} upgraded a settlement to a city at {}.".format(
            self.agent.agent_name, str(self.node))

    def __call__(self, game):
        raise NotImplementedError()


class UpgradeSettlementFactory(ActionFactory):
    action_type = ActionType.UpgradeSettlement

    def __call__(self, game, agent):
        """Returns a list of available actions of type action_type for the player.

        Args:
            game: A catan.game.Game object.
            agent_id: Agent id for the agend that.

        Returns:
            List of legal action of type action_type.
        """
        raise NotImplementedError()