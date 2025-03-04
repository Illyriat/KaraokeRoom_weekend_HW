import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Asleep In The Deep", "Mastodon", "2014")

    def test_find_song_by_name(self):
        self.assertEqual("Asleep In The Deep", self.song.title)

    def test_song_by_artist(self):
        self.assertEqual("Mastodon", self.song.artist)

    def test_song_by_year(self):
        self.assertEqual("2014", self.song.year)
