from ...context import catan

import unittest


class TestEndTrading(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.game = catan.game.Game()
        setup = catan.setup.default.DefaultGameSetup()
        setup(self.game)
        self.agent = catan.agent.Agent(agent_name="Bob")
        self.action = catan.action.end_trading.EndTrading(self.agent, None)
    
    def testObservation(self):
        observation = self.action.observation()
        self.assertListEqual(observation, [self.agent.id])


class TestEndTradingFactory(unittest.TestCase):
    def setUp(self):
        pass

    def testTest(self):
        pass