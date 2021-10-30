from ..context import catan

import unittest


class TestGameObject(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.object = catan.shared.GameObject()

    def testSchema(self):
        self.assertIsInstance(self.object.schema, catan.shared.Schema)

    def testId(self):
        self.assertEqual(self.object.id, "default.0")