from ..context import catan

import unittest


class TestConnections(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.connection = catan.graph.Connection()

    def testConnect(self):
        self.assertFalse(self.connection(0, 1))
        self.assertFalse(self.connection(1, 0))
        self.connection.connect(0, 1)
        self.assertTrue(self.connection(0, 1))
        self.assertFalse(self.connection(1, 0))

    def testBidirectionalConnect(self):
        self.connection = catan.graph.Connection(bidirectional=True)
        self.assertFalse(self.connection(0, 1))
        self.assertFalse(self.connection(1, 0))
        self.connection.connect(0, 1)
        self.assertTrue(self.connection(0, 1))
        self.assertTrue(self.connection(1, 0))

    def testDisconnect(self):
        self.connection.connect(0, 1)
        self.assertTrue(self.connection(0, 1))
        self.connection.disconnect(0, 1)
        self.assertFalse(self.connection(0, 1))

    def testBidirectionalDisconnect(self):
        self.connection = catan.graph.Connection(bidirectional=True)
        self.connection.connect(0, 1)
        self.assertTrue(self.connection(0, 1))
        self.assertTrue(self.connection(1, 0))
        self.connection.disconnect(0, 1)
        self.assertFalse(self.connection(0, 1))
        self.assertFalse(self.connection(1, 0))

    def testObservation(self):
        self.connection.connect(0, 1)
        forward, backward = self.connection.observation()
        self.assertListEqual(forward[0], [0])
        self.assertListEqual(forward[1], [1])
        self.assertListEqual(backward[0], [1])
        self.assertListEqual(backward[1], [0])

    def testBidirectionalObservation(self):
        self.connection = catan.graph.Connection(bidirectional=True)
        self.connection.connect(0, 1)
        forward = self.connection.observation()[0]
        self.assertListEqual(sorted(forward[0]), [0, 1])
        self.assertListEqual(sorted(forward[1]), [0, 1])

    def testNeighbors(self):
        self.assertListEqual(list(self.connection.neighbors(0)), [])
        self.connection.connect(0, 1)
        self.assertListEqual(list(self.connection.neighbors(0)), [1])


class TestGraph(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.graph = catan.graph.Graph()

    def testAddGameObjects(self):
        self.graph.addGameObjects(["object_a", "object_b"])
        self.assertListEqual(self.graph.game_object_ids, ["object_a", "object_b"])
        self.assertDictEqual(self.graph.game_object_mapping, {"object_a":0, "object_b":1})

    def testAddConnectionType(self):
        connection_type = catan.graph.ConnectionType.Owns
        self.graph.addConnectionType(connection_type)

    def testAddConnectionTypeError(self):
        with self.assertRaises(TypeError):
            self.graph.addConnectionType(None)

    def testConnect(self):
        connection_type = catan.graph.ConnectionType.Owns
        self.graph.addConnectionType(connection_type)
        self.graph.addGameObjects(["object_a", "object_b"])
        self.assertFalse(self.graph(connection_type, "object_a", "object_b"))
        self.graph.connect(connection_type, "object_a", "object_b")
        self.assertTrue(self.graph(connection_type, "object_a", "object_b"))

    def testDisconnect(self):
        connection_type = catan.graph.ConnectionType.Owns
        self.graph.addConnectionType(connection_type)
        self.graph.addGameObjects(["object_a", "object_b"])
        self.graph.connect(connection_type, "object_a", "object_b")
        self.assertTrue(self.graph(connection_type, "object_a", "object_b"))
        self.graph.disconnect(connection_type, "object_a", "object_b")
        self.assertFalse(self.graph(connection_type, "object_a", "object_b"))

    def testObservation(self):
        connection_type = catan.graph.ConnectionType.Owns
        self.graph.addConnectionType(connection_type)
        self.graph.addGameObjects(["object_a", "object_b"])
        self.graph.connect(connection_type, "object_a", "object_b")
        object_ids, observation = self.graph.observation()
        forward, backward = observation[connection_type]
        self.assertListEqual(forward[0], [0])
        self.assertListEqual(forward[1], [1])
        self.assertListEqual(backward[0], [1])
        self.assertListEqual(backward[1], [0])

    def testNeighbors(self):
        connection_type = catan.graph.ConnectionType.Owns
        self.graph.addConnectionType(connection_type)
        self.graph.addGameObjects(["object_a", "object_b"])
        self.assertListEqual(list(self.graph.neighbors(connection_type, "object_a")), [])
        self.graph.connect(connection_type, "object_a", "object_b")
        self.assertListEqual(list(self.graph.neighbors(connection_type, "object_a")), ["object_b"])

