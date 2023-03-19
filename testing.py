import unittest

from main1 import autoclaveStatus

class Test(unittest.TestCase):
    def test_autoclaveStatus(self):
        self.assertEqual(autoclaveStatus(10), 10)