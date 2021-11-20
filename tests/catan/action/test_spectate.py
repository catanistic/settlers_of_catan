from catan import action
from ...context import catan

import unittest


class TestSpectate(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.agent = catan.agent.Agent(agent_name="Alice")
        self.spectator = catan.agent.Agent(agent_name="Bob")
        action = catan.action.roll_dice.RollDice(self.agent.id, None)
        self.action = catan.action.spectate.Spectate(self.spectator.id, None, action)
    
    def testObservation(self):
        action_type, observation = self.action.observation()
        self.assertEqual(action_type, catan.action.roll_dice.RollDice)
        self.assertListEqual(observation, [self.agent.id])


class TestSpectateFactory(unittest.TestCase):
    def setUp(self):
        pass

    def testTest(self):
        pass