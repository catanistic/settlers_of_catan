from catan.graph import Graph, ConnectionType
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


class Game():
    def __init__(self, victory_points=10, logging_callbacks=None):
        super().__init__()
        self.ids = {object_type:set() for object_type in GameObjectType}
        self.game_objects = {}

        self.graph = Graph()
        for connection_type in ConnectionType:
            self.graph.addConnectionType(connection_type)

        game_state = GameState()
        self.game_state_id = game_state.id
        self.addGameObject(game_state)

        self.victory_points = victory_points
        self.done = False
        self.action_history = []

        self.agent_order = []
        self.curr_agent_index = 0

        self.logging_callbacks = logging_callbacks 

    @property
    def curr_agent_id(self):
        return self.agent_order[self.curr_agent_index]
    
    def addGameObject(self, game_object):
        self.ids[game_object.game_object_type].add(game_object.id)
        self.game_objects[game_object.id] = game_object
        self.graph.addGameObjects([game_object.id])

    @property
    def action_space(self):
        if self.state is not None:
            return self.state.action_space

    def step(self, action):
        self.action_history.append(action)
        action(self)
        if self.logging_callbacks is not None:
            for logging_callback in self.logging_callbacks:
                logging_callback(str(action))

    @property
    def reward(self):
        previous_agent_id = self.action_history[-1].agent_id
        return self.game_objects[previous_agent_id].reward

    def observation(self):
        observations = {
            object_id:self.game_objects[object_id].observation() for object_id in self.game_objects
        }
        graph = self.graph.observation()
        return observations, graph