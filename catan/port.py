from catan.shared import GameObject, FieldType
from catan.resource import ResourceType


class Port(GameObject):
    def __init__(self):
        super().__init__()
        self.resource = ResourceType.Everything
        self.exchange_rate = 3

    def observation(self, spectator_id=None):
        return []
