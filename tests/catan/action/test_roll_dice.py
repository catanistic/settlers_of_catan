from ...context import catan

import unittest


class TestRollDice(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.agent = catan.agent.Agent(agent_name="Bob")
        print(self.agent.id)
        self.action = catan.action.roll_dice.RollDice(self.agent.id, None)