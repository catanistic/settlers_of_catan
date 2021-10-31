from catan.shared import GameObject, GameObjectType, FieldType


class Road(GameObject):
    game_object_type = GameObjectType.Road

    def __init__(self):
        super().__init__()