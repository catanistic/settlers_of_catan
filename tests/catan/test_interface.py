from ..context import catan

import unittest


class TestInterface(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.game = catan.game.Game()