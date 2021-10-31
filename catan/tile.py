from catan.shared import GameObject, GameObjectType, FieldType


class Tile(GameObject):
    game_object_type = GameObjectType.Tile

    def __init__(self, resource_type):
        super().__init__()
        self.resource_type = resource_type