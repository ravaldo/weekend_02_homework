
class Guest():
	def __init__(self, name, wallet, fav_song, allergies=None):
		if allergies is None: allergies = []
		self.name = name
		self.wallet = wallet
		self.fav_song = fav_song
		self.food_allergies = allergies
		
	def has_enough_money(self, amount):
		return amount <= self.wallet
	
	def purchase(self, amount):
		if self.has_enough_money(amount):
			self.wallet -= amount
	
