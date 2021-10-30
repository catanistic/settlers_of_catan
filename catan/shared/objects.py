from catan.shared.schema import Schema

from enum import Enum, auto


class GameObjectType(Enum):
    Action = "action"
    Actor = "actor" 
    Connector = "connector"
    GameState = "shared_state" 
    Node = "node" 
    Port = "port" 
    Tile = "tile" 
    Default = "default"


class GameObject():
    game_object_type = GameObjectType.Default

    def __init__(self, object_id=0):
        self.schema = Schema()
        self.object_id = object_id

    @property
    def id(self):
        """Returns unique id of the game object.
        """
        return "{}.{}".format(self.game_object_type.value, self.object_id)

    @property
    def observation(self):
        """Returns observation that is pertinent to the object.
        """
        raise NotImplementedError()