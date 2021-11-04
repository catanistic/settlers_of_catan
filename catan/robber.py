from catan.shared import GameObject, GameObjectType, FieldType


class Robber(GameObject):
    game_object_type = GameObjectType.Robber

    def __init__(self):
        super().__init__()
        self.position = None