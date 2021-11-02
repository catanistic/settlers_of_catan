from ..context import catan

import unittest


class TestAgent(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.agent = catan.agent.Agent()

    def testSetUp(self):
        pass