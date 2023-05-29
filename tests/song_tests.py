import unittest
from classes.song import *

class SongTest(unittest.TestCase):
	
	def setUp(self):
		self.song = Song("Bohemian Rhapsody", "Queen")
		
	def test_song_has_name(self):
		self.assertEqual("Bohemian Rhapsody", self.song.name)
                        
	def test_song_has_artist(self):
		self.assertEqual("Queen", self.song.artist)
