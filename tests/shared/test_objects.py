from ..context import catan

import unittest


class TestGameObject(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.object = catan.shared.GameObject()

    def testSchema(self):
        self.assertIsInstance(self.object.schema, catan.shared.Schema)

    def testId(self):
        self.object.game_object_type = catan.shared.GameObjectType.Agent
        self.assertTrue(self.object.id.startswith("agent"))
        self.object = catan.shared.GameObject()
        self.object.game_object_type = catan.shared.GameObjectType.Agent
        self.assertTrue(self.object.id.startswith("agent"))
