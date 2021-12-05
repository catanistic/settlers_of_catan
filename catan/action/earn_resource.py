from catan.action.base import Action, ActionFactory
from catan.resource import ResourceType
from catan.shared import FieldType 


class EarnResource(Action):
    def __init__(self, agent, next_state, amount, resource_type):
        super().__init__(agent, next_state)
        self.resource_type = resource_type
        self.amount = amount
        self.schema.append_field("resource_type", FieldType.Category, ResourceType)
        self.schema.append_field("amount", FieldType.Integer)

    def observation(self, spectator=None):
        return self.schema(
            agent_id=self.agent.id,
            resource_type=self.resource_type,
            amount=self.amount
        )

    def __str__(self):
        return "{} earned {} card(s) of type {}.".format(
            self.agent.agent_name,
            self.amount, self.resource_type.value
        )

    def __call__(self, game):
        game.game_state.resources[self.resource_type] -= self.amount
        self.agent.resources[self.resource_type] += self.amount
        game.state = self.next_state


class EarnResourceFactory(ActionFactory):
    def __init__(self, game, agent, next_state, dice_roll):
        super().__init__(game, agent, next_state)
        self.dice_roll = dice_roll

    def __call__(self):
        """Returns a list of available actions of type action_type for the player.

        Returns:
            List of legal action of type action_type.
        """
        raise NotImplementedError()