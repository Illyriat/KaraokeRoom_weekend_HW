import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Pod", 4, 7)

    def test_room_name(self):
        self.assertEqual("Pod", self.room.name)

    def test_room_capacity(self):
        self.assertEqual(7, self.room.capacity)

    def test_sign_in_guest(self):
        self.room.sign_in_guest(self)
        self.assertEqual([self], self.room.guest)

    def test_sign_out_guest(self):
        self.room.sign_out_guest(self)
        self.assertEqual([], self.room.guest)

    def test_add_toons(self):
        song = Song("Gone Sovereign", "Stone Sour", "2012")
        self.room.add_toons(song)
        self.assertEqual([song], self.room.song_list)