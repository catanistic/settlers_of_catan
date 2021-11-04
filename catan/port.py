from catan.shared import GameObject, GameObjectType, FieldType
from catan.resource import ResourceType


class Port(GameObject):
    game_object_type = GameObjectType.Port

    def __init__(self):
        super().__init__()
        self.resource = ResourceType.Everything
        self.exchange_rate = 3