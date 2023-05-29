import unittest
from classes.menuItem import *

class MenuItemTest(unittest.TestCase):
	
	def setUp(self):
		self.item = MenuItem("Chicken Wings", 8, ["Eggs", "Wheat"])
		
	def test_item_has_name(self):
		self.assertEqual("Chicken Wings", self.item.name)
        
	def test_item_has_price(self):
		self.assertEqual(8, self.item.price)
        
	def test_guest_has_allergens(self):
		self.assertEqual(True, "Eggs" in self.item.allergens)
	
