from catan.card import ValidDevelopmentCardTypes
from catan.resource import ValidResourceTypes
from catan.shared import GameObject, GameObjectType, FieldType


class Agent(GameObject):
    game_object_type = GameObjectType.Agent

    def __init__(self, agent_name=None):
        super().__init__()
        self.agent_name = agent_name if agent_name else str(self.object_id)
        self.resources = {r:0 for r in ValidResourceTypes}
        self.development_cards = {c:0 for c in ValidDevelopmentCardTypes}
        self.development_cards_buffer = {c:0 for c in ValidDevelopmentCardTypes}
        self.played_development_cards = {c:0 for c in ValidDevelopmentCardTypes}

    @property
    def id(self):
        return "{}.{}".format(super().id, self.agent_name)

    def __str__(self):
        return "Player ({})".format(self.agent_name)

    @property
    def resource_count(self):
        return sum(self.resources[r] for r in ValidResourceTypes)

    @property
    def reward(self):
        return 0

    @property
    def victory_points(self):
        return 0

    def observation(self, spectator_id=None):
        if spectator_id == self.id:
            return
        else:
            return