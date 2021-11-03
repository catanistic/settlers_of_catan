from ..context import catan

import unittest


class TestNode(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.Node = catan.node.Node((0, 0))