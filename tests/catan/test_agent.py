from ..context import catan

import unittest


class TestAgent(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.agent = catan.agent.Agent("Alice")

    def testSchema(self):
        pass

    def testCanAfford(self):
        self.agent.resources[catan.resource.ResourceType.Clay] += 1
        self.assertTrue(self.agent.canAfford({catan.resource.ResourceType.Clay:1}))
        self.assertFalse(self.agent.canAfford({catan.resource.ResourceType.Clay:2}))

    def testPay(self):
        resource_type = catan.resource.ResourceType.Clay
        self.agent.resources[resource_type] += 1
        game = catan.game.Game()
        self.agent.pay({resource_type:1}, game)
        self.assertEqual(self.agent.resources[resource_type], 0)
        self.assertEqual(game.game_state.resources[resource_type], 1)