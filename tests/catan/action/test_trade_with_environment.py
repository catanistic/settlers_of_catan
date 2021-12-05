from ...context import catan

import unittest


class TestTradeWithEnvironment(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.game = catan.game.Game()
        setup = catan.setup.default.DefaultGameSetup()
        setup(self.game)
        self.agent = catan.agent.Agent(agent_name="Bob")
        self.resource_in = catan.resource.ResourceType.Wheat
        self.resource_out = catan.resource.ResourceType.Wool
        self.action = catan.action.trade_with_environment.TradeWithEnvironment(
            self.agent, None, 4, self.resource_in, self.resource_out)
    
    def testObservation(self):
        observation = self.action.observation()
        self.assertListEqual(observation, [self.agent.id, 4])


class TestUpgradeSettlementFactory(unittest.TestCase):
    def setUp(self):
        pass

    def testTest(self):
        pass