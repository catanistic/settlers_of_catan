from catan.action.base import ActionType, Action, ActionFactory
from catan.node import NodeState
from catan.resource import ResourceType
from catan.shared import FieldType 


CITY_PRICE = {
    ResourceType.Clay: 1,
    ResourceType.Wheat: 1,
    ResourceType.Wood: 1,
    ResourceType.Wool: 1,
}


class UpgradeSettlement(Action):
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
        self.node.state = NodeState.City
        self.agent.pay(self.price, game)
        # TODO: add agent reward.
        game.state = self.next_state


class UpgradeSettlementFactory(ActionFactory):
    def __call__(self):
        """Returns a list of available actions of type action_type for the player.

        Returns:
            List of legal action of type action_type.
        """
        raise NotImplementedError()