
class Room():
	def __init__(self, number, max_guests, entry_fee):
		self.number = number
		self.max_guests = max_guests
		self.playlist = []
		self.entry_fee = entry_fee
		self.till = 100
		self.guests = []
		self.menu = []

	def find_song_by_name_string(self, searchTerm):
		for s in self.playlist:
			if searchTerm.lower() in s.name.lower():
				return s
	
	def find_songs_by_artist(self, searchTerm):
		return [s for s in self.playlist if s.artist.lower() in searchTerm.lower()]
		
	def is_room_full(self):
		return len(self.guests) >= self.max_guests
	
	def number_of_guests(self):
		return len(self.guests)
		
	def check_in_guest(self, guest):
		if not self.is_room_full() and guest.has_enough_money(self.entry_fee):
			self.guests.append(guest)
			guest.purchase(self.entry_fee)
			self.till += self.entry_fee
			s = self.find_song_by_name_string(guest.fav_song.name)
			if s is not None:
				return("woohoo!")

	def check_out_guest(self, guest):
		self.guests.remove(guest)
	
	def sell_guest_menu_item(self, item, guest):
		if item in self.menu:
			if guest.has_enough_money(item.price):
				if any(x in item.allergens for x in guest.food_allergies):
					return
				else:
					guest.purchase(item.price)
					self.till += item.price


			

