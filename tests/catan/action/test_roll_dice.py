from ...context import catan

import unittest


class TestRollDice(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.agent = catan.agent.Agent(agent_name="Bob")
        self.action = catan.action.roll_dice.RollDice(self.agent.id, None)

    def testObservation(self):
        observation = self.action.observation(self.agent.id)
        self.assertListEqual(observation, [self.agent.id])


class TestRollDiceFactory(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.agent = catan.agent.Agent(agent_name="Bob")
        self.factory = catan.action.roll_dice.RollDiceFactory()

    def testActionSpace(self):
        actions = self.factory(None, self.agent.id, None)
        self.assertEqual(len(actions), 1)
        self.assertIsInstance(actions[0], catan.action.roll_dice.RollDice)
