from ...context import catan
from catan.shared.objects import GameObjectType
from catan.graph import ConnectionType

from collections import Counter
import unittest


class TestBaseSetup(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.game = catan.game.Game()
        self.setup = catan.setup.base.GameSetup()
        self.setup.setup(self.game)

    def testRoads(self):
        road_ids = list(self.game.ids[GameObjectType.Road])
        self.assertEqual(len(road_ids), 72)

        roads_with_num_neighbors = []
        for road_id in road_ids:
            node_ids = self.game.graph.neighbors(ConnectionType.RoadNextToNode, road_id)
            road_neighbors = self.game.graph.neighbors(ConnectionType.RoadNeighbor, road_id)
            self.assertEqual(len(node_ids), 2)
            roads_with_num_neighbors.append(len(road_neighbors))
        roads_with_num_neighbors = Counter(roads_with_num_neighbors)
        self.assertDictEqual(roads_with_num_neighbors, {2:6, 3:24, 4:42})

    def testPorts(self):
        port_ids = list(self.game.ids[GameObjectType.Port])
        self.assertEqual(len(port_ids), 9)

        port_counts = []
        for node_id in self.game.ids[GameObjectType.Node]:
            port_ids_ = self.game.graph.neighbors(ConnectionType.NextToPort, node_id)
            port_counts += list(port_ids_)
        port_counts = Counter(port_counts)
        for port_id in port_ids:
            self.assertEqual(port_counts[port_id], 2)

    def testNodes(self):
        node_ids = list(self.game.ids[GameObjectType.Node])
        self.assertEqual(len(node_ids), 54)

        node_num_neighbors = []
        for node_id in node_ids:
            neighbors = self.game.graph.neighbors(ConnectionType.NodeNeighbor, node_id)
            node_num_neighbors.append(len(neighbors))
        node_num_neighbors = Counter(node_num_neighbors)
        self.assertDictEqual(node_num_neighbors, {2:18, 3:36})

    def testTiles(self):
        tile_ids = list(self.game.ids[GameObjectType.Tile])
        self.assertEqual(len(tile_ids), 19)

        for tile_id in tile_ids:
            node_ids = self.game.graph.neighbors(ConnectionType.TileNextToNode, tile_id)
            self.assertEqual(len(node_ids), 6)

    def testSetRobberPosition(self):
        self.setup.setRobberPosition(self.game, (0,0))
        robber_id = self.setup.robber.id
        node_ids = self.game.graph.neighbors(ConnectionType.RobberNextToNode, robber_id)
        self.assertEqual(len(node_ids), 6)