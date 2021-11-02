from catan.graph import Graph
from catan.resource import ValidResourceTypes
from catan.card import DevelopmentCardType
from catan.shared.objects import GameObject, GameObjectType
from catan.shared.schema import FieldType


class GameState(GameObject):
    game_object_type = GameObjectType.GameState

    def __init__(self):
        super().__init__()
        self.resources = {}
        for resource in ValidResourceTypes:
            self.resources[resource] = 0        
            self.schema.append_field(resource.value, FieldType.Integer)

        self.schema.append_field("development_cards", FieldType.Integer)
        self.development_cards = {
            card: 0 for card in DevelopmentCardType
        }

    def observation(self):
        observation = {}
        for resource in ValidResourceTypes:
            observation[resource.value] = int(self.resources[resource] > 0)
        observation["development_cards"] = sum(self.development_cards[card] for card in DevelopmentCardType)
        return self.schema(**observation)


class Game(GameObject):
    def __init__(self):
        super().__init__()
        self.ids = {object_type:set() for object_type in GameObjectType}
        self.game_objects = {}
        self.graph = Graph()

        game_state = GameState()
        self.game_state_id = game_state.id
        self.addGameObject(game_state)
    
    def addGameObject(self, game_object):
        self.ids[game_object.game_object_type].add(game_object.id)
        self.game_objects[game_object.id] = game_object

    def observation(self):
        observation = {
            object_id:self.game_objects[object_id].observation() for object_id in self.game_objects
        }
        graph = self.graph.observation()
        return observation, graph