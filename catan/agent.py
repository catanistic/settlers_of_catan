from catan.shared import GameObject, GameObjectType, FieldType


class Agent(GameObject):
    game_object_type = GameObjectType.Agent

    def __init__(self, agent_name=None):
        super().__init__()
        self.agent_name = agent_name if agent_name else str(self.object_id)
        self.resources = {}
        self.development_cards = {}
        self.played_development_cards = {}

    @property
    def reward(self):
        return 0

    @property
    def victory_points(self):
        return 0

    def observation(self):
        pass