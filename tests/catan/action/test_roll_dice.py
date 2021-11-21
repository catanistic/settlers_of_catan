from ...context import catan

import unittest


class TestRollDice(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.agent = catan.agent.Agent(agent_name="Bob")
        self.action = catan.action.roll_dice.RollDice(self.agent, None)

    def testObservation(self):
        observation = self.action.observation(self.agent.id)
        self.assertListEqual(observation, [self.agent.id])


class TestRollDiceFactory(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.agent = catan.agent.Agent(agent_name="Bob")

    def testActionSpace(self):
        factory = catan.action.roll_dice.RollDiceFactory(None, self.agent, None)
        actions = factory()
        self.assertEqual(len(actions), 1)
        self.assertIsInstance(actions[0], catan.action.roll_dice.RollDice)
