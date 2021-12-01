from catan.action.base import ActionType, Action, ActionFactory
from catan.graph import ConnectionType
from catan.node import NodeState
from catan.resource import ResourceType
from catan.shared import FieldType 


SETTLEMENT_PRICE = {
    ResourceType.Clay: 1,
    ResourceType.Wheat: 1,
    ResourceType.Wood: 1,
    ResourceType.Wool: 1,
}

class BuildSettlement(Action):
    action_type = ActionType.BuildSettlement

    def __init__(self, agent, next_state, node, is_free=False):
        super().__init__(agent, next_state)
        self.node = node
        self.is_free = is_free
        self.price = SETTLEMENT_PRICE
        self.schema.append_field("node_id", FieldType.GameObjectReference)
        self.schema.append_field("is_free", FieldType.Integer)

    def observation(self, spectator=None):
        return self.schema(
            agent_id=self.agent.id,
            node_id=self.node.id,
            is_free=int(self.is_free),
        )

    def __str__(self):
        free_modifier = " (for free)" if self.is_free else ""
        return "{} has build a settlement{} at {}.".format(
            self.agent.agent_name, free_modifier, str(self.node))

    def __call__(self, game):
        self.node.owner = self.agent
        self.node.state = NodeState.Settlement
        game.graph.connect(ConnectionType.Owns, self.agent.id, self.node.id)

        # Disconnect neighbor roads with different owner.
        neighbor_road_ids = game.graph.neighbors(ConnectionType.NodeNextToRoad, self.node.id)
        for road_id in neighbor_road_ids:
            neighbor_road = game.game_objects[road_id]
            if neighbor_road.occupied and neighbor_road.owner != self.agent:
                game.graph.disconnect(ConnectionType.NodeNextToRoad, self.node.id, road_id)
        
        # Disconnect neighbor nodes with different owner.
        neighbor_node_ids = game.graph.neighbors(ConnectionType.NodeNeighbor, self.node.id)
        for node_id in neighbor_node_ids:
            neighbor_node = game.game_objects[node_id]
            if neighbor_node.occupied and neighbor_node.owner != self.agent:
                game.graph.disconnect(ConnectionType.NodeNeighbor, self.node.id, node_id)

        # TODO: add agent reward.

        if not self.is_free:
            self.agent.pay(self.price, game)

        game.state = self.next_state


class BuildSettlementFactory(ActionFactory):
    action_type = ActionType.BuildSettlement

    def __call__(self):
        """Returns a list of available actions of type action_type for the player.

        Returns:
            List of legal action of type action_type.
        """
        raise NotImplementedError()