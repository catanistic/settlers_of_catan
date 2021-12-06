from catan.graph import ConnectionType
from catan.node import Node
from catan.port import Port
from catan.road import Road
from catan.robber import Robber
from catan.tile import Tile
from catan.resource import ValidResourceTypes
from catan.card import DevelopmentCardType

TILES_PER_ROW = [3, 4, 5, 4, 3]
PORT_NODES = [
    [(0, 2), (0, 3)],
    [(0, 5), (0, 6)],
    [(1, 8), (2, 9)],
    [(3, 9), (4, 8)],
    [(5, 6), (5, 5)],
    [(5, 3), (5, 2)],
    [(4, 0), (4, 1)],
    [(3, 0), (2, 0)],
    [(1, 0), (1, 1)],
]

DEVELOPMENT_CARDS = {
    DevelopmentCardType.Knight: 14,
    DevelopmentCardType.YearOfPlenty: 2,
    DevelopmentCardType.RoadBuilding: 2,
    DevelopmentCardType.VictoryPoint: 5,
    DevelopmentCardType.Monopoly: 2,
}

def calculateNumberOfNodesAt(row):
    previous_level_tiles = TILES_PER_ROW[row- 1] if 0 <= row - 1 else 0
    curr_level_tiles = TILES_PER_ROW[row] if row < len(TILES_PER_ROW) else 0
    return max(curr_level_tiles, previous_level_tiles) * 2 + 1


def calculateNumberOfRoadsAt(row):
    return calculateNumberOfNodesAt(row) - 1


class GameSetup():
    def __init__(self):
        self.nodes = None
        self.tiles = None
        self.roads = None
        self.side_roads = None
        self.ports = None
        self.robber = None

    def _generateTiles(self, game):
        self.tiles = []
        for row, num_tiles in enumerate(TILES_PER_ROW):
            self.tiles.append([Tile((row, col)) for col in range(num_tiles)])

        for tiles in self.tiles:
            for tile in tiles:
                game.addGameObject(tile)

    def _generateNodes(self, game):
        self.nodes = []
        for row in range(len(TILES_PER_ROW) + 1):
            self.nodes.append([Node((row, col)) for col in range(calculateNumberOfNodesAt(row))])

        for nodes in self.nodes:
            for node in nodes:
                game.addGameObject(node)

    def _generateRoads(self, game):
        self.roads = []
        for row in range(len(TILES_PER_ROW) + 1):
            self.roads.append([Road((row, col)) for col in range(calculateNumberOfRoadsAt(row))])

        for roads in self.roads:
            for road in roads:
                game.addGameObject(road)

        self.side_roads = []
        for row, num_tiles in enumerate(TILES_PER_ROW):
            self.side_roads.append([Road((row + 0.5, col)) for col in range(num_tiles + 1)])

        for roads in self.side_roads:
            for road in roads:
                game.addGameObject(road)
    
    def _generatePorts(self, game):
        self.ports = [Port() for _ in range(len(PORT_NODES))]
        for port in self.ports:
            game.addGameObject(port)

    def _addTileNodeConnections(self, game):
        connection_type = ConnectionType.TileNextToNode
        for row, tiles in enumerate(self.tiles):
            for col, tile in enumerate(tiles):
                for n_row in range(row, row + 2):
                    for n_col in range(2 * col, 2 * col + 3):
                        node = self.nodes[n_row][n_col]
                        game.graph.connect(connection_type, tile.id, node.id)

    def _addNodeNodeConnections(self, game):
        connection_type = ConnectionType.NodeNeighbor
        road_connection = ConnectionType.NodeNextToRoad

        # Node neighbors in the same "row"
        for row, nodes in enumerate(self.nodes):
            for col, node in enumerate(nodes[:-1]):
                neighbor = self.nodes[row][col + 1]
                game.graph.connect(connection_type, node.id, neighbor.id)

                road = self.roads[row][col]
                road.nodes += [node, neighbor]
                game.graph.connect(road_connection, node.id, road.id)
                game.graph.connect(road_connection, neighbor.id, road.id)

        # Node neighbors from different "rows"
        from_correction = [1, 1, 1, 0, 0, 0]
        to_correction = [0, 0, 0, 0, 1, 1]
        for row in range(1, len(self.nodes)):
            nodes = self.nodes[row]
            for col in range(0, len(nodes) - from_correction[row], 2):
                node = nodes[col + from_correction[row]]
                neighbor = self.nodes[row - 1][col + to_correction[row]]
                game.graph.connect(connection_type, node.id, neighbor.id)

                road = self.side_roads[row - 1][col // 2]
                road.nodes += [node, neighbor]
                game.graph.connect(road_connection, node.id, road.id)
                game.graph.connect(road_connection, neighbor.id, road.id)

    def _addRoadRoadConnections(self, game):
        connection_type = ConnectionType.RoadNeighbor

        # Road neighbors in the same "row"
        for row, roads in enumerate(self.roads):
            for col, road in enumerate(roads[:-1]):
                neighbor = self.roads[row][col + 1]
                game.graph.connect(connection_type, road.id, neighbor.id)

        # Road neighbors in the "verticals".
        up_correction = [-1, -1, -1, 0, 0]
        down_correction = [0, 0, -1, -1, -1]
        for row, roads in enumerate(self.side_roads):
            for col, road in enumerate(roads):
                for n_row, correction in enumerate((up_correction[row], down_correction[row])):
                    n_row += row
                    for n_col in range(2 * col + correction, 2 * col + 2 + correction):
                        if 0 <= n_col < len(self.roads[n_row]):
                            neighbor = self.roads[n_row][n_col]
                            game.graph.connect(connection_type, road.id, neighbor.id)

    def _addPortConnections(self, game):
        connection_type = ConnectionType.NextToPort
        for i, positions in enumerate(PORT_NODES):
            for position in positions:
                row, col = position
                game.graph.connect(connection_type, self.nodes[row][col].id, self.ports[i].id)

    def setRobberPosition(self, game, position):
        row, col = position
        tile = self.tiles[row][col]
        self.robber.tile_id = tile.id
        self.robber.position = position
        node_ids = game.graph.neighbors(ConnectionType.TileNextToNode, tile.id)
        for node_id in node_ids:
            game.graph.connect(ConnectionType.RobberNextToNode, self.robber.id, node_id)

    def _addInitialDevelopmentCards(self, game):
        for card_type, count in DEVELOPMENT_CARDS.items():
            game.game_state.development_cards[card_type] = count

    def _addInitialResourceCards(self, game):
        for resource_type in ValidResourceTypes:
            game.game_state.resources[resource_type] = 19

    def _distributeInitialResources(self, game):
        pass

    def __call__(self, game):
        # Generating Game Objects
        self._generateTiles(game)
        self._generateNodes(game)
        self._generateRoads(game)
        self._generatePorts(game)
        # Initialize resource and development cards
        self._addInitialResourceCards(game)
        self._addInitialDevelopmentCards(game)
        # Deal out cards to each player
        self._distributeInitialResources(game)

        self.robber = Robber()
        game.addGameObject(self.robber)

        # Adding graph connections
        self._addTileNodeConnections(game)
        self._addNodeNodeConnections(game)
        self._addRoadRoadConnections(game)
        self._addPortConnections(game)