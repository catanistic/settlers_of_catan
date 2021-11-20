from ...context import catan

import unittest


class TestEarnResource(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.agent = catan.agent.Agent(agent_name="Bob")
        self.action = catan.action.earn_resource.EarnResource(self.agent, None, 1,
            catan.resource.ResourceType.Wheat)
    
    def testObservation(self):
        observation = self.action.observation(self.agent.id)
        expected_type = self.action.schema.category_mappings["resource_type"][catan.resource.ResourceType.Wheat]
        self.assertListEqual(observation, [self.agent.id, expected_type, 1])


class TestEarnResourceFactory(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.agent = catan.agent.Agent(agent_name="Bob")
        self.action = catan.action.earn_resource.EarnResource(self.agent, None, 1,
            catan.resource.ResourceType.Wheat)
    
    def testActionSpace(self):
        observation = self.action.observation(self.agent.id)
        expected_type = self.action.schema.category_mappings["resource_type"][catan.resource.ResourceType.Wheat]
        self.assertListEqual(observation, [self.agent.id, expected_type, 1])
