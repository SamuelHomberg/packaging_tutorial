import unittest
from example_package_samuelhomberg.example import add_one


class TestExample(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(add_one(2), 3)