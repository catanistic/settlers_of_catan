from catan.shared import GameObject, GameObjectType, FieldType

class Agent(GameObject):
    game_object_type = GameObjectType.Actor

    def __init__(self, actor_name):
        super().__init__()
        self.actor_name = actor_name

    @property
    def id(self):
        return "{}.{}".format(super().id, self.actor_name)

    @property
    def observation(self):
        pass