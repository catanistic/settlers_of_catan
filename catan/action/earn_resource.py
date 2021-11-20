from catan.action.base import ActionType, Action, ActionFactory
from catan.resource import ResourceType
from catan.shared import FieldType 


class EarnResource(Action):
    action_type = ActionType.EarnResource

    def __init__(self, agent_id, next_state, amount, resource_type):
        super().__init__(agent_id, next_state)
        self.resource_type = resource_type
        self.amount = amount
        self.schema.append_field("resource_type", FieldType.Category, ResourceType)
        self.schema.append_field("amount", FieldType.Integer)

    def observation(self, spectator_id=None):
        return self.schema(
            agent_id=self.agent_id,
            resource_type=self.resource_type,
            amount=self.amount
        )

    def __str__(self):
        return "{} earned {} card(s) of type {}.".format(
            self.agent_id.split(".")[-1],
            self.amount, self.resource_type.value
        )

    def __call__(self, game):
        raise NotImplementedError()


class EarnResourceFactory(ActionFactory):
    action_type = ActionType.EarnResource

    def __call__(self, game, agent_id):
        raise NotImplementedError()