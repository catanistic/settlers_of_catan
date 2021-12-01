from ...context import catan

import unittest


class TestBuildSettlement(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.game = catan.game.Game()
        setup = catan.setup.default.DefaultGameSetup()
        setup(self.game)
        node_ids = self.game.ids[catan.node.Node]
        node_id = next(iter(node_ids))
        self.node = self.game.game_objects[node_id]
        self.agent = self.game.agent_order[0]
        self.action = catan.action.build_settlement.BuildSettlement(self.agent, None, self.node)
    
    def testObservation(self):
        observation = self.action.observation()
        self.assertListEqual(observation, [self.agent.id, self.node.id, 0])


class TestBuildSettlementFactory(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.game = catan.game.Game()
        setup = catan.setup.default.DefaultGameSetup()
        setup(self.game)

    def testTest(self):
        pass