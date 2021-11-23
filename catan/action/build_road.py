from catan.action.base import Action, ActionFactory
from catan.graph import ConnectionType
from catan.road import Road
from catan.shared import FieldType 


class BuildRoad(Action):
    def __init__(self, agent, next_state, road, is_free=False):
        super().__init__(agent, next_state)
        self.road = road 
        self.is_free = is_free
        self.schema.append_field("road_id", FieldType.GameObjectReference)
        self.schema.append_field("is_free", FieldType.Integer)

    def observation(self, spectator=None):
        return self.schema(
            agent_id=self.agent.id,
            road_id=self.road.id,
            is_free=int(self.is_free),
        )

    def __str__(self):
        free_modifier = " (for free)" if self.is_free else ""
        return "{} has build a road{} at {}.".format(
            self.agent.agent_name, free_modifier, str(self.road))

    def __call__(self, game):
        # Set road owner.
        self.road.owner = self.agent
        game.graph.connect(ConnectionType.Owns, self.agent.id, self.road.id)

        # Disconnect neighbor roads with different owner.
        neighbor_road_ids = game.graph.neighbors(ConnectionType.RoadNeighbor, self.road.id)
        for road_id in neighbor_road_ids:
            neighbor_road = game.game_objects[road_id]
            if neighbor_road.occupied and neighbor_road.owner != self.agent:
                game.graph.disconnect(ConnectionType.RoadNeighbor, self.road.id, road_id)

        # Disconnect neighbor nodes with different owner.
        for node in self.road.nodes:
            if node.occupied and node.owner != self.agent:
                game.graph.disconnect(ConnectionType.NodeNextToRoad, node.id, self.road.id)

        # TODO: add node "booking" mechanism when 2 roads from same agent are neighbors.

        # TODO: trigger longest road check for current agent.

        # TODO: subtract resources from the agent for building a road.

        game.state = self.next_state


class BuildRoadFactory(ActionFactory):
    def __init__(self, game, agent, next_state, is_free=False, node=None, road_number=1):
        super().__init__(game, agent, next_state)
        self.is_free = is_free
        self.node = node
        self.road_number = road_number
        self.curr_road = 1

    def __call__(self):
        """Returns a list of available actions of type action_type for the player.

        Returns:
            List of legal action of type action_type.
        """
        next_state = self.next_state if self.curr_road == self.road_number else self
        self.curr_road += 1

        if not self.node is None:
            available_road_ids = self.game.graph.neighbors(ConnectionType.NodeNextToRoad, self.node.id)
        else:
            owned_objects_ids = self.game.graph.neighbors(ConnectionType.Owns, self.agent.id)
            road_ids = self.game.ids[Road]
            print(road_ids)
            
        raise NotImplementedError()