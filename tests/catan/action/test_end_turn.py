from ...context import catan

import unittest


class TestEndTurn(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.game = catan.game.Game()
        setup = catan.setup.default.DefaultGameSetup()
        setup(self.game)
        self.agent = catan.agent.Agent(agent_name="Bob")
        self.action = catan.action.end_turn.EndTurn(self.agent, None)
    
    def testObservation(self):
        observation = self.action.observation()
        self.assertListEqual(observation, [self.agent.id])


class TestEndTurnFactory(unittest.TestCase):
    def setUp(self):
        pass

    def testTest(self):
        pass