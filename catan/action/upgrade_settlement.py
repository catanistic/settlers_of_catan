from catan.action.base import ActionType, Action, ActionFactory
from catan.shared import FieldType 


class UpgradeSettlement(Action):
    action_type = ActionType.UpgradeSettlement

    def __init__(self, agent_id, next_state, location_id):
        super().__init__(agent_id, next_state)
        self.location_id = location_id
        self.schema.append_field("location_id", FieldType.GameObjectReference)

    def observation(self, spectator_id=None):
        return self.schema(
            agent_id=self.agent_id,
            location_id=self.location_id,
        )

    def __str__(self):
        return "{} upgraded a settlement to a city at {}.".format(
            self.agent_id.split(".")[-1], self.location_id.split(".")[-1])

    def __call__(self, game):
        raise NotImplementedError()


class UpgradeSettlementFactory(ActionFactory):
    action_type = ActionType.UpgradeSettlement

    def action_space(self, game, agent_id):
        """Returns a list of available actions of type action_type for the player.

        Args:
            game: A catan.game.Game object.
            agent_id: Agent id for the agend that.

        Returns:
            List of legal action of type action_type.
        """
        raise NotImplementedError()