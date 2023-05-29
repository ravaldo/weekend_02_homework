import unittest
from classes.guest import *
from classes.song import *

class GuestTest(unittest.TestCase):
	
	def setUp(self):
		self.song = Song("Bohemian Rhapsody", "Queen")
		self.tom = Guest("Tom", 50, self.song)
		
	def test_guest_has_name(self):
		self.assertEqual("Tom", self.tom.name)
        
	def test_guest_has_money(self):
		self.assertEqual(50, self.tom.wallet)
        
	def test_guest_has_fav_song(self):
		self.assertEqual("Bohemian Rhapsody", self.tom.fav_song.name)
	
	def test_guest_has_enough_money_positive(self):
		self.assertEqual(True, self.tom.has_enough_money(50))
		
	def test_guest_has_enough_money_negative(self):
		self.assertEqual(False, self.tom.has_enough_money(51))
	
	def test_guest_purchase(self):
		self.tom.purchase(20)
		self.assertEqual(30, self.tom.wallet)
		
	def test_guest_purchase_fail(self):
		self.tom.purchase(60)
		self.assertEqual(50, self.tom.wallet)
	
	def test_guest_has_allergy(self):
		self.assertEqual([], self.tom.food_allergies)
