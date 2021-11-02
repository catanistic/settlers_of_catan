from ..context import catan

import unittest


class TestPort(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.port = catan.port.Port()