from catan.action.base import ActionType, Action, ActionFactory
from catan.shared import FieldType 


class BuildRoad(Action):
    action_type = ActionType.BuildRoad

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
        raise NotImplementedError()


class BuildRoadFactory(ActionFactory):
    action_type = ActionType.BuildRoad

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
        raise NotImplementedError()