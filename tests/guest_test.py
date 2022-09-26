import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Martin Schmidt", 40, "Count of Tuscany")

    def test_guest_name(self):
        self.assertEqual("Martin Schmidt", self.guest.name)

    def test_guest_funds(self):
        self.assertEqual(40, self.guest.funds)

    def test_favourite_song(self):
        self.assertEqual("Count of Tuscany", self.guest.favourite_song)