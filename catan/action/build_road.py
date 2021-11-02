from catan.action.base import ActionType, Action, ActionFactory
from catan.shared import FieldType 


class BuildRoad(Action):
    action_type = ActionType.BuildRoad

    def __init__(self, agent_id, next_state, location_id, is_free=False):
        super().__init__(agent_id, next_state)
        self.location_id = location_id
        self.is_free = is_free
        self.schema.append_field("location_id", FieldType.GameObjectReference)
        self.schema.append_field("is_free", FieldType.Integer)

    def observation(self, spectator_id=None):
        return self.schema(
            agent_id=self.agent_id,
            location_id=self.location_id,
            is_free=int(self.is_free),
        )

    def __str__(self):
        free_modifier = " (for free)" if self.is_free else ""
        return "{} has build a road{} at {}.".format(
            self.agent_id.split(".")[-1], free_modifier, self.location_id.location_id.split(".")[-1])

    def __call__(self, game):
        raise NotImplementedError()


class BuildRoadFactory(ActionFactory):
    action_type = ActionType.BuildRoad

    def action_space(self, game, agent_id):
        """Returns a list of available actions of type action_type for the player.

        Args:
            game: A catan.game.Game object.
            agent_id: Agent id for the agend that.

        Returns:
            List of legal action of type action_type.
        """
        raise NotImplementedError()