from ...context import catan

import unittest


class TestBaseSetup(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.game = catan.game.Game()
        self.setup = catan.setup.base.GameSetup()
        self.setup.setup(self.game)

    def testSetUp(self):
        pass