from enum import Enum, auto


class ConnectionType(Enum):
    NextPlayer = auto() 
    NextToPort = auto()
    NodeNeighbor = auto()
    Owns = auto()
    RoadNeighbor = auto() 
    RoadNextToNode = auto()
    RobberNextToNode = auto()
    TileNextToNode = auto()


IsBidirectional = {
    ConnectionType.NextPlayer:False,
    ConnectionType.NextToPort:False,
    ConnectionType.NodeNeighbor:True,
    ConnectionType.Owns:False,
    ConnectionType.RoadNeighbor:True,
    ConnectionType.RoadNextToNode:False,
    ConnectionType.RobberNextToNode:False,
    ConnectionType.TileNextToNode:False,
}


class Connection():
    def __init__(self, bidirectional=False):
        self.bidirectinal = bidirectional
        self.connections = {}

    def __call__(self, idx_a, idx_b):
        if idx_a in self.connections:
            return idx_b in self.connections[idx_a]
        return False

    def neighbors(self, idx):
        if idx in self.connections:
            return self.connections[idx].copy()
        return set()

    def _connect(self, idx_a, idx_b):
        if idx_a not in self.connections:
            self.connections[idx_a] = set()
        self.connections[idx_a].add(idx_b)

    def connect(self, idx_a, idx_b):
        self._connect(idx_a, idx_b)
        if self.bidirectinal:
            self._connect(idx_b, idx_a)

    def _disconnect(self, idx_a, idx_b):
        if idx_a in self.connections:
            self.connections[idx_a].remove(idx_b)
    
    def disconnect(self, idx_a, idx_b):
        self._disconnect(idx_a, idx_b)
        if self.bidirectinal:
            self._disconnect(idx_b, idx_a)

    def observation(self):
        edge_heads = []
        edge_tails = []
        for head in self.connections:
            for tail in self.connections[head]:
                edge_heads.append(head)
                edge_tails.append(tail)

        forward_edges = [edge_heads, edge_tails]
        if self.bidirectinal:
            return [forward_edges]
        backward_edges = [edge_tails[:], edge_heads[:]]
        return [forward_edges, backward_edges]


class Graph():
    def __init__(self, game_object_ids=None):
        self.game_object_ids = []
        self.game_object_mapping = {}
        self.addGameObjects(game_object_ids)
        self.connections = {}

    def _convertToIds(self, object_id_a, object_id_b):
        return self.game_object_mapping[object_id_a], self.game_object_mapping[object_id_b]

    def _typecheckConnectionType(self, connection_type):
        if type(connection_type) is not ConnectionType:
            raise TypeError("Connection type should ConnectionType.")

    def __call__(self, connection_type, object_id_a, object_id_b):
        self._typecheckConnectionType(connection_type)
        idx_a, idx_b = self._convertToIds(object_id_a, object_id_b)
        return self.connections[connection_type](idx_a, idx_b)
    
    def neighbors(self, connection_type, object_id):
        self._typecheckConnectionType(connection_type)
        neighbors = self.connections[connection_type].neighbors(self.game_object_mapping[object_id])
        return {self.game_object_ids[n] for n in neighbors}

    def connect(self, connection_type, object_id_a, object_id_b):
        self._typecheckConnectionType(connection_type)
        idx_a, idx_b = self._convertToIds(object_id_a, object_id_b)
        self.connections[connection_type].connect(idx_a, idx_b)

    def disconnect(self, connection_type, object_id_a, object_id_b):
        self._typecheckConnectionType(connection_type)
        idx_a, idx_b = self._convertToIds(object_id_a, object_id_b)
        self.connections[connection_type].disconnect(idx_a, idx_b)
    
    def addConnectionType(self, connection_type):
        self._typecheckConnectionType(connection_type)
        self.connections[connection_type] = Connection(IsBidirectional[connection_type])
    
    def addGameObjects(self, game_object_ids):
        if game_object_ids is None:
            return

        if type(game_object_ids) is str:
            game_object_ids = [game_object_ids]

        for game_object_id in game_object_ids:
            if game_object_id not in self.game_object_mapping:
                self.game_object_mapping[game_object_id] = len(self.game_object_ids)
                self.game_object_ids.append(game_object_id)

    def observation(self):
        observation = {}
        for connection_type in self.connections:
            observation[connection_type] = self.connections[connection_type].observation()
        return self.game_object_ids[:], observation