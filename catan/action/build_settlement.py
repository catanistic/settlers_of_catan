from catan.action.base import ActionType, Action, ActionFactory
from catan.shared import FieldType 


class BuildSettlement(Action):
    action_type = ActionType.BuildSettlement

    def __init__(self, agent, next_state, node, is_free=False):
        super().__init__(agent, next_state)
        self.node = node
        self.is_free = is_free
        self.schema.append_field("node_id", FieldType.GameObjectReference)
        self.schema.append_field("is_free", FieldType.Integer)

    def observation(self, spectator_id=None):
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
        raise NotImplementedError()


class BuildSettlementFactory(ActionFactory):
    action_type = ActionType.BuildSettlement

    def __call__(self, game, agent):
        """Returns a list of available actions of type action_type for the player.

        Args:
            game: A catan.game.Game object.
            agent_id: Agent id for the agend that.

        Returns:
            List of legal action of type action_type.
        """
        raise NotImplementedError()