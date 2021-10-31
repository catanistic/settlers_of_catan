from catan.shared import GameObject, GameObjectType, FieldType

from enum import Enum


class NodeState(Enum):
    Empty = "empty"
    Settlement = "settlement"
    Castle = "castle"


class Node(GameObject):
    game_object_type = GameObjectType.Node

    def __init__(self):
        super().__init__()