from ..context import catan

import unittest


class TestGameState(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.game_state = catan.game.GameState()

    def testObservation(self):
        pass


class TestGame(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.game = catan.game.Game()

    def testAddGameObject(self):
        game_object = catan.agent.Agent()
        self.game.addGameObject(game_object)
        observations, _ = self.game.observation()
        self.assertEqual(len(observations), 2)

    def testObservation(self):
        observations, _ = self.game.observation()
        self.assertEqual(len(observations), 1)