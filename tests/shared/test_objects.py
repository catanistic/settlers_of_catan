from ..context import catan

import unittest


class TestGameObject(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.object = catan.shared.GameObject()

    def testSchema(self):
        self.assertIsInstance(self.object.schema, catan.shared.Schema)

    def testId(self):
        id_1 = self.object.id
        self.assertIsInstance(self.object.id, int)
        self.object = catan.shared.GameObject()
        id_2 = self.object.id
        self.assertIsInstance(self.object.id, int)
        self.assertNotEqual(id_1, id_2)
