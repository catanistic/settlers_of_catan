from catan.resource import ResourceType
from catan.shared import GameObject, GameObjectType, FieldType


class Tile(GameObject):
    game_object_type = GameObjectType.Tile

    def __init__(self, position, resource_type=ResourceType.Null):
        super().__init__()
        self.resource_type = resource_type
        self.position = position

    def __str__(self):
        return "Tile at {} of type {}".format(self.position, self.resource_type.value)