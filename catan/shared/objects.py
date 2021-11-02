from catan.shared.schema import Schema

from enum import Enum


class GameObjectType(Enum):
    Agent = "agent" 
    GameState = "shared_state" 
    Node = "node" 
    Port = "port" 
    Road = "road"
    Robber = "robber"
    Tile = "tile" 


def id_generator():
    id = 0
    while True:
        yield id
        id += 1


class GameObject():
    game_object_type = None
    id_generator = id_generator()

    def __init__(self):
        self.schema = Schema()
        self.object_id = next(self.id_generator)

    @property
    def id(self):
        """Returns unique id of the game object.
        """
        return "{}.{}".format(self.game_object_type.value, self.object_id)

    def observation(self):
        """Returns observation that is pertinent to the object.
        """
        raise NotImplementedError()