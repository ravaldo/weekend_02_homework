import unittest
from classes.song import *
from classes.guest import *
from classes.room import *
from classes.menuItem import *


class RoomTest(unittest.TestCase):
	
	def setUp(self):
		
		self.song1 = Song("Bohemian Rhapsody", "Queen")
		self.song2 = Song("Billie Jean", "Michael Jackson")
		self.song3 = Song("Stairway to Heaven", "Led Zeppelin")
		self.song4 = Song("Rocket Man", "Elton John")
		self.song5 = Song("Da Funk", "Daft Punk")
		self.song6 = Song("Get Lucky", "Daft Punk")
				
		self.wings = MenuItem("Chicken Wings", 10, ["Eggs", "Wheat"])
		self.nachos = MenuItem("Nachos", 8, ["Dairy"])
		
		self.alice = Guest("Alice", 50, self.song1)
		self.bob = Guest("Bob", 20, self.song2)
		self.charlie = Guest("Charlie", 15, self.song5)
		
		self.room1 = Room(1, 2, 20)
		self.room2 = Room(2, 4, 15)
		
		self.room2.menu.append(self.wings)
		self.room2.menu.append(self.nachos)
		
		self.room1.playlist = [self.song1, self.song2, self.song3, self.song4]
		self.room2.playlist = [self.song2, self.song3, self.song4, self.song5, self.song6]
	
	def test_room_has_number(self):
		self.assertEqual(1, self.room1.number)
	
	def test_room_has_entry_fee(self):
		self.assertEqual(15, self.room2.entry_fee)
	
	def test_room_has_song_positve(self):
		s = self.room1.find_song_by_name_string("Billie Jean")
		self.assertEqual(True, isinstance(s, Song))
		self.assertEqual("Billie Jean", s.name)
	
	def test_room_has_songs_by_artist(self):
		songs = self.room2.find_songs_by_artist("Daft Punk")
		self.assertEqual(2, len(songs))
		self.assertEqual(True, self.song5.name in [s.name for s in songs])
		self.assertEqual(True, self.song6.name in [s.name for s in songs])
	
	def test_room_checkin_max_occupancy(self):
		val1 = self.room1.check_in_guest(self.alice)
		val2 = self.room1.check_in_guest(self.bob)
		val3 = self.room1.check_in_guest(self.charlie)
		self.assertEqual("woohoo!", val1)
		self.assertEqual("woohoo!", val2)
		self.assertEqual(None, val3)
		self.assertEqual(2, self.room1.number_of_guests())
		self.assertEqual(True, self.room1.is_room_full())
		self.assertEqual(140, self.room1.till)
		self.assertEqual(30, self.alice.wallet)
		self.assertEqual(0, self.bob.wallet)
		self.assertEqual(15, self.charlie.wallet)
		
		
	def test_room_checkin_guest_can_afford(self):
		val1 = self.room2.check_in_guest(self.alice)
		val2 = self.room2.check_in_guest(self.bob)
		val3 = self.room2.check_in_guest(self.charlie)
		self.assertEqual("woohoo!", val3)
		self.assertEqual(3, self.room2.number_of_guests())
		self.assertEqual(False, self.room2.is_room_full())
		
		self.room2.sell_guest_menu_item(self.wings, self.alice)
		self.room2.sell_guest_menu_item(self.nachos, self.charlie)
		
		self.assertEqual(155, self.room2.till)		# 15+15+15+10
		self.assertEqual(25, self.alice.wallet) 	# 50-15-10
		self.assertEqual(0, self.charlie.wallet)	# 15-15
	
	def test_room_checkout(self):
		self.room2.check_in_guest(self.alice)
		self.room2.check_in_guest(self.bob)
		self.room2.check_in_guest(self.charlie)
		self.room2.check_out_guest(self.bob)
		
		self.assertEqual(2, self.room2.number_of_guests())
		self.assertEqual(False, self.room2.is_room_full())
		self.assertEqual(True, self.alice in self.room2.guests)
		self.assertEqual(False, self.bob in self.room2.guests)
		self.assertEqual(True, self.charlie in self.room2.guests)

	def test_room_guest_allergy_failed_purchase(self):
		self.alice.food_allergies.append("Wheat")
		self.alice.food_allergies.append("Soya")
		self.room2.check_in_guest(self.alice)
		self.room2.sell_guest_menu_item(self.wings, self.alice)
		
		self.assertEqual(115, self.room2.till)
		self.assertEqual(35, self.alice.wallet)
		
		