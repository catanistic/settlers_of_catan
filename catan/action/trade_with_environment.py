from catan.action.base import Action, ActionFactory
from catan.node import NodeState
from catan.resource import ResourceType
from catan.shared import FieldType 


class TradeWithEnvironment(Action):
    def __init__(self, agent, next_state, num_agent_resources, resource_type_in, resourcde_type_out):
        super().__init__(agent, next_state)
        self.num_agent_resources = num_agent_resources
        self.resource_type_in = resource_type_in
        self.resource_type_out = resourcde_type_out
        self.schema.append_field("num_agent_resources", FieldType.Integer)

    def observation(self, spectator=None):
        return self.schema(
            agent_id=self.agent.id,
            num_agent_resources=self.num_agent_resources,
        )

    def __str__(self):
        return "{} traded {} of {} for 1 {}.".format(
            self.agent.agent_name, self.num_agent_resources, self.resource_type_in, self.resource_type_out)

    def __call__(self, game):
        game.game_state.resources[self.resource_type_in] += self.num_agent_resources
        self.agent.resources[self.resource_type_in] -= self.num_agent_resources
        game.game_state.resources[self.resource_type_out] -= 1
        self.agent.resources[self.resource_type_out] += 1
        game.state = self.next_state


class TradeWithEnvironmentFactory(ActionFactory):
    def __call__(self):
        """Returns a list of available actions of type action_type for the player.

        Returns:
            List of legal action of type action_type.
        """
        raise NotImplementedError()