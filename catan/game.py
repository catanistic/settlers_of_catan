from catan.agent import Agent
from catan.card import DevelopmentCardType
from catan.graph import Graph, ConnectionType
from catan.resource import ValidResourceTypes
from catan.shared.objects import GameObject
from catan.shared.schema import FieldType
from catan.state.spectate import SpectateGameState


import numpy as np 


class GameState(GameObject):
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
    def __init__(self, victory_points=10, agent_names=None, logging_callbacks=None):
        """Initializes the game.

        Args:
            victory_points: number of points required for the victory.
            agent_names: the list of agent names.
            logging_callbacks: a list of logging callbacks.
        """
        super().__init__()
        self.ids = {}
        self.game_objects = {}

        self.graph = Graph()
        for connection_type in ConnectionType:
            self.graph.addConnectionType(connection_type)

        self.game_state = GameState()
        self.game_state_id = self.game_state.id
        self.addGameObject(self.game_state)

        self.victory_points = victory_points
        self.done = False
        self.action_history = []

        if agent_names is None:
            agent_names = ["Alice"]
        self.agent_order = [Agent(agent_name=name) for name in agent_names]
        np.random.shuffle(self.agent_order)
        self.curr_agent_index = 0

        self.logging_callbacks = logging_callbacks 

    @property
    def curr_agent(self):
        return self.agent_order[self.curr_agent_index]
    
    def addGameObject(self, game_object):
        if game_object.__class__ not in self.ids:
            self.ids[game_object.__class__] = set()
        self.ids[game_object.__class__].add(game_object.id)
        self.game_objects[game_object.id] = game_object
        self.graph.addGameObjects([game_object.id])

    @property
    def action_space(self):
        if self.state is not None:
            return self.state.action_space

    def step(self, action):
        if type(self.state) is SpectateGameState:
            self.action_history.append(action)
            action(self)
            if self.logging_callbacks is not None:
                for logging_callback in self.logging_callbacks:
                    logging_callback(str(action))
        else:
            self.state = SpectateGameState(action)
            self.step(self.state.action_space[0])

    @property
    def reward(self):
        return self.action_history[-1].agent.reward

    def observation(self):
        observations = {
            object_id:self.game_objects[object_id].observation() for object_id in self.game_objects
        }
        graph = self.graph.observation()
        return observations, graph