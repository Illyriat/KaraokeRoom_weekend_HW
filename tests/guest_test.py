import unittest
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Martin Schmidt", 40, "Count of Tuscany")

        self.songs = [
            Song("Count of Tuscany", "Dream Theater", "2009"),
            Song("Killing Floor", "Black Stone Cherry", "2011")
        ]

    def test_guest_name(self):
        self.assertEqual("Martin Schmidt", self.guest.name)

    def test_guest_funds(self):
        self.assertEqual(40, self.guest.funds)

    def test_favourite_song(self):
        self.assertEqual("Count of Tuscany", self.guest.favourite_song)

    def test_guest_can_afford_True(self):
        self.assertEqual(True, self.guest.can_afford(30))

    def test_guest_can_afford_False(self):
        self.assertEqual(False, self.guest.can_afford(50))

    def test_guest_can_pay_amount(self):
        self.guest.pay_amount(7)
        self.assertEqual(33, self.guest.funds)

    def test_guest_cheers_when_fav_song__True(self):
        self.assertEqual("Whoo!", self.guest.cheer_for_song(self.songs))

    def test_guest_cheers_when_fav_song__False(self):
        guest1 = Guest("Kerry", 20, "Wrong Song")
        self.assertEqual(None, guest1.cheer_for_song(self.songs))
