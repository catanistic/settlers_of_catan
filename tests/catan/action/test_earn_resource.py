from ...context import catan

import unittest


class TestEarnResource(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.agent = catan.agent.Agent(agent_name="Bob")
        self.action = catan.action.earn_resource.EarnResource(self.agent.id, None, 1,
            catan.resource.ResourceType.Wheat)
    
    def test_setup(self):
        pass