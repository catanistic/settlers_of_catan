from ..context import catan

import unittest


class TestRoad(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.game = catan.road.Road()