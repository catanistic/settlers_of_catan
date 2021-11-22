from catan.shared import GameObject, FieldType

from enum import Enum


class NodeState(Enum):
    Empty = "empty"
    Settlement = "settlement"
    City = "city"


class Node(GameObject):
    def __init__(self, position):
        super().__init__()
        self.state = NodeState.Empty
        self.position = position

    def __str__(self):
        return "{}".format(self.position)