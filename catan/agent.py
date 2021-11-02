from catan.shared import GameObject, GameObjectType, FieldType


class Agent(GameObject):
    game_object_type = GameObjectType.Agent

    def __init__(self, agent_name=None):
        super().__init__()
        self.agent_name = agent_name if agent_name else str(self.object_id)
        self.resources = {}
        self.development_cards = {}
        self.played_development_cards = {}

    def observation(self):
        pass