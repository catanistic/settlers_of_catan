from ...context import catan

import unittest


class TestUpgradeSettlement(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.game = catan.game.Game()
        setup = catan.setup.default.DefaultGameSetup()
        setup(self.game)
        node_ids = self.game.ids[catan.node.Node]
        node_id = next(iter(node_ids))
        self.node = self.game.game_objects[node_id]
        self.agent = catan.agent.Agent(agent_name="Bob")
        self.action = catan.action.build_settlement.BuildSettlement(self.agent, None, self.node)
    
    def testObservation(self):
        observation = self.action.observation()
        self.assertListEqual(observation, [self.agent.id, self.node.id, 0])


class TestUpgradeSettlementFactory(unittest.TestCase):
    def setUp(self):
        pass

    def testTest(self):
        pass