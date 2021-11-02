from catan.shared import GameObject, GameObjectType, FieldType

from enum import Enum


class NodeState(Enum):
    Empty = "empty"
    Settlement = "settlement"
    City = "city"


class Node(GameObject):
    game_object_type = GameObjectType.Node

    def __init__(self):
        super().__init__()
        self.state = NodeState.Empty