from ...context import catan

import unittest


class TestSpectate(unittest.TestCase):
    def setUp(self):
        super().setUp()
        agent = catan.agent.Agent(agent_name="Alice")
        self.agent = catan.agent.Agent(agent_name="Bob")
        action = catan.action.roll_dice.RollDice(agent.id, None)
        self.action = catan.action.spectate.Spectate(self.agent.id, None, action)
    
    def testSetup(self):
        pass