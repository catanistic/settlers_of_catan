from ..context import catan

import unittest


class TestRobber(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.robber = catan.robber.Robber()