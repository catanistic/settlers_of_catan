from ...context import catan

import unittest


class TestEndGame(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.game = catan.game.Game()
        setup = catan.setup.default.DefaultGameSetup()
        setup(self.game)
        self.agent = catan.agent.Agent(agent_name="Bob")
        self.action = catan.action.end_game.EndGame(self.agent, None, 0)
    
    def testObservation(self):
        observation = self.action.observation()
        self.assertListEqual(observation, [self.agent.id])


class TestEndGameFactory(unittest.TestCase):
    def setUp(self):
        pass

    def testTest(self):
        pass