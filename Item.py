class Item:
	def __init__(self, fsishort: str, fsilong: str, description: str, upc: str, category: str, status: str, sbstyle: str, qty_available: int, price: float):
		self.fsishort = fsishort
		self.fsilong = fsilong
		self.name = ''  # Parsed from description
		self.description = description
		self.size = ''  # Parsed from description
		self.color = ''  # Parsed from description
		self.upc = upc
		self.category = category
		self.status = status
		self.qty_available = qty_available
		self.price = price
		self.sbstyle = sbstyle
		self.pattern = ''  # Parsed from description
		self.patterns = ["Stripe", "Micro Stripe", "Pin Stripe", "Stripe Hybrid", "Solid Hybrid", "Classic Stripe", "Pencil Stripe", "Aloha", "Elephant Ear", "Pique", "Elefante", "Elephant", "Floral", "Jungle Cat", "Key Largo", "Pineapple", "Shark Teeth", "Tropicool", "X-Ray Palm", "Banana Leaf", "Cabana Stripes", "Flying Fish", "Flyfish", "Geometric", "Cashmere VNeck", "Micro", "Terry", "Pant", "Hybrid", "Trunk", "Mosaic", "Bamboo", "Under the Sea", "Multi Leaf", "Camo", "Coral", "Cashmere Hoodie", "Solid"]
		self.names = ["William", "Alexander", "Anthony", "Adam", "Bingo", "Boys", "Boardshort", "Christopher", "Phillip", "Cortland", "Coleman", "Ace", "McQueen", "Jack", "George", "Sun Shirt", "Trunk", "Walking Short", "Shirt", "Sheet"]
		#  Note: Micro is used as a pattern and a name.
		#  Note: Alex == Alexander
		self.categories = ["Tops", "Sweaters", "Boys Tops", "Boys Swim", "Swim", "Bottoms", "Layering"]
		self.colors = ["True Blue and White", "Nautical Stripe", "True Blue", "Blue & White", "Washed Blue", "Pink", "Light Pink", "Mint", "Navy", "Royal Blue", "Royal Blue", "Sky Blue", "White", "Delphinium", "Atlantic", "Green Apple", "Coral", "French Blue", "Happy Pink", "Indigo", "Lemon Yellow", "Gold", "Fog", "Red", "Various", "Orange", "Kelly", "Sweet Pea", "Blue/White", "Green", "Purple", "Red", "Multi", "Turqoise", "Yellow", "Dk Blue", "Lt Blue", "Denim", "Indigo/White", "Ship", "Camp Green", "Stone", "Sunny Yellow", "Darkest Indigo", "Dk Indigo", "Grass", "Day Lilly", "Cranberry", "Sunshine Yellow", "Fire Coral", "Ocean"]
		self.colors.sort()
		self.colors.sort(key=len, reverse=True)
		self.names.sort()
		self.names.sort(key=len, reverse=True)
		self.categories.sort()
		self.categories.sort(key=len, reverse=True)
		self.patterns.sort()
		self.patterns.sort(key=len, reverse=True)
		#  Note: Camo Ocean is to be split into Camo pattern, Ocean color.
		#  Note: Delph == Delphinium
		#  Note: Sky == Sky Blue.
		#  Note: Royal == Royal Blue.
		#  Note: Coral is a color and a pattern.
		#  Note: Turq == Turqoise

		self.sizes = ["42", "40", "38", "36", "34", "32", "30", "12", "10", "8", "6", "4", "XXL", "XL", "L", "M", "S", "XS"]
		self.__parse_description()

	def __parse_description(self):
		d = self.description
		for pat in self.patterns:
			if 'CORAL' in d.upper():
				for c in self.colors:
					if c.upper() in d.upper() and c.upper() != 'CORAL':
						self.pattern = 'Coral'
						break
			elif pat.upper() in d.upper():
				self.pattern = pat
				break
		for n in self.names:
			if 'BOY\'S' in d.upper():
				self.name = 'Boys'
				break
			if n.upper() in d.upper():
				self.name = n
				break
		for cat in self.categories:
			if cat.upper() in d.upper():
				self.category = cat
				break
		for color in self.colors:
			if "DELPH" in d.upper():
				self.color = "Delphinium"
				break
			elif "WASH BLUE" in d.upper():
				self.color = "Washed Blue"
				break
			elif "SKY" in d.upper():
				self.color = "Sky Blue"
				break
			elif "ROYAL" in d.upper():
				self.color = "Royal Blue"
				break
			elif "TURQ" in d.upper():
				self.color = "Turqoise"
				break
			elif "CORAL" in d.upper():
				if self.pattern == '':
					self.color = 'Coral'
					break
			elif color.upper() in d.upper():
				self.color = color
				break
		for s in self.sizes:
			if 'XXLARGE' in d.upper():
				self.size = 'XXL'
				break
			elif 'XLARGE' in d.upper():
				self.size = 'XL'
				break
			elif 'XSMALL' in d.upper():
				self.size = 'XS'
				break
			elif 'SMALL' in d.upper():
				self.size = 'S'
				break
			elif 'MEDIUM' in d.upper():
				self.size = 'M'
				break
			elif 'LARGE' in d.upper():
				self.size = 'L'
				break
			elif ' ' + s in d[-4:]:
				self.size = s
				break

	def get_category(self):
		return self.category

	def get_color(self):
		return self.color

	def get_sbstyle(self):
		return self.sbstyle

	def get_upc(self):
		return self.upc

	def get_fsishort(self):
		return self.fsishort

	def get_description(self):
		return self.description

	def get_qty(self):
		return self.qty_available

	def get_price(self):
		return self.price

	def __str__(self):
		padding = 30
		header = ["|FSI Short#|", "|FSI Long#|", "|Name|", "|Pattern|", "|Description|", "|Size|", "|Color|", "|UPC|", "|Category|", "|Status|", "|SB-Style|", "|Qty Available|", "|Price|"]
		values = [self.fsishort, self.fsilong, self.name, self.pattern, self.description, self.size, self.color, self.upc, self.category, self.status, self.sbstyle, self.qty_available, str(self.price)]
		hstring = ''
		vstring = ''

		for counter in range(0, len(header)):
			h = header[counter]
			v = values[counter]
			if counter == any({0, 1, 2, 3, 6}):
				hstring += h.ljust(int(padding * 0.75), ' ')
				vstring += v.ljust(int(padding * 0.75), ' ')
			elif counter == 4:
				hstring += h.ljust(int(padding * 1.5), ' ')
				vstring += v.ljust(int(padding * 1.5), ' ')
			else:
				hstring += h.ljust(padding, ' ')
				vstring += v.ljust(padding, ' ')

		return hstring + '\n' + vstring + '\n'

