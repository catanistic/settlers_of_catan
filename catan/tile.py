from catan.resource import ResourceType
from catan.shared import GameObject, GameObjectType, FieldType


PROBABILITIES = {
    0: 0,
    2: 0.0278,
    3: 0.0556,
    4: 0.0833,
    5: 0.1111,
    6: 0.1389,
    7: 0.1667,
    8: 0.1389,
    9: 0.1111,
    10: 0.0833,
    11: 0.0556,
    12: 0.0278, 
}


class Tile(GameObject):
    game_object_type = GameObjectType.Tile

    def __init__(self, position, resource_type=ResourceType.Null):
        super().__init__()
        self.resource_type = resource_type
        self.number_token = 0
        self.position = position
    
    @property
    def probability(self):
        return PROBABILITIES[self.number_token]

    def __str__(self):
        return "Tile at {} of type {}".format(self.position, self.resource_type.value)