class Item:
	def __init__(self, fsishort: str, fsilong: str, description: str, upc: str, category: str, status: str, sbstyle: str, qty_available: int, price: float):
		self.fsishort = fsishort
		self.fsilong = fsilong
		self.style = ''  # Parsed from description
		self.description = description
		self.size = ''  # Parsed from description
		self.color = ''  # Parsed from description
		self.upc = upc
		self.category = category
		self.status = status
		self.qty_available = qty_available
		self.price = price
		self.sbcatalog = sbstyle
		self.pattern = ''  # Parsed from description
		self.patterns = sorted(["Stripe", "Micro Stripe", "Microstripe Jersey", "Pin Stripe", "Stripe Hybrid", "Solid Hybrid", "Classic Stripe", "Pencil Stripe", "Aloha", "Elephant Ear", "Pique", "Elefante", "Elephant", "Floral", "Jungle Cat", "Key Largo", "Pineapple", "Shark Teeth", "Tropicool", "X-Ray Palm", "Banana Leaf", "Cabana Stripes", "Flying Fish", "Flyfish", "Geometric", "Cashmere VNeck", "Micro", "Terry", "Hybrid", "Mosaic", "Bamboo", "Under the Sea", "Multi Leaf", "Camo", "Coral", "Cashmere Hoodie", "Solid"], key=len, reverse=True)
		self.styles = sorted(["William", "Alexander", "Anthony", "Adam", "Bingo", "Boys", "Classic Boardshort", "Classic Swimtrunk", "Boardshort", "Christopher", "Phillip", "Cortland", "Coleman", "Coleman Pant", "Ace", "McQueen", "Jack", "George", "Sun Shirt", "Trunk", "Walking Short", "Shirt", "Sheet", "Short"], key=len, reverse=True)
		#  Note: Micro is used as a pattern and a name.
		#  Note: Alex == Alexander
		self.categories = sorted(["Tops", "Sweaters", "Boys Tops", "Boys Swim", "Swim", "Bottoms", "Layering"], key=len, reverse=True)
		self.colors = sorted(["True Blue and White", "True Blue/White", "Nautical Stripe", "Blue", "True Blue", "Blue & White", "Washed Blue", "Washed Blue/White", "Darkest Indigo/Navy", "Pink", "Light Pink", "Mint", "Navy", "Royal Blue", "Sky Blue", "White", "Delphinium", "Delphinium/White", "Bermuda Green", "Atlantic", "Green Apple", "Coral", "French Blue", "Happy Pink", "Indigo", "Lemon Yellow", "Gold", "Fog", "Red", "Various", "Orange", "Kelly", "Sweet Pea", "Blue/White", "Pink/White", "Green", "Purple", "Red", "Multi", "Turqoise", "Yellow", "Dk Blue", "Lt Blue", "Denim", "Indigo/White", "Ship", "Camp Green", "Stone", "Sunny Yellow", "Grass Court", "Deep Blue", "Vivid Blue", "Darkest Indigo", "Dk Indigo", "Grass", "Day Lilly", "Cranberry", "Sunshine Yellow", "Fire Coral", "Ocean"], key=len, reverse=True)

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
			if 'MULTI-LEAF' in d.upper():
				self.pattern = 'Multi Leaf'
				break
			if 'UNDERSEA' in d.upper():
				self.pattern = 'Under the Sea'
				break
			if 'CORAL' in d.upper():
				for c in self.colors:
					if c.upper() in d.upper() and c.upper() != 'CORAL':
						self.pattern = 'Coral'
						break
			elif pat.upper() in d.upper():
				self.pattern = pat
				break
		for n in self.styles:
			if 'CLASSIC SWIM TRUNK' in d.upper():
				self.style = 'Classic Swimtrunk'
				break
			elif 'CLASSIC BOARD SHORT' in d.upper():
				self.style = 'Classic Boardshort'
				break
			elif 'BOARD SHORT' in d.upper():
				self.style = 'Boardshort'
				break
			elif 'BOY\'S' in d.upper():
				self.style = 'Boys'
				break
			elif n.upper() in d.upper():
				self.style = n
				break
		for cat in self.categories:
			if cat.upper() in d.upper():
				self.category = cat
				break
		for color in self.colors:
			if "MULTI" in d.upper():
				for c in self.colors:
					if c.upper() in d.upper() and c.upper() != "MULTI":
						self.color = c
						break
				else:
					self.color = 'Multi'
					break
			elif "DELPH " in d.upper():  # Space after DELPH is important.
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
				if self.pattern == 'Coral':
					for c in self.colors:
						if c.upper() in d.upper() and c.upper() != 'CORAL':
							self.color = c
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

	def get_style(self):
		return self.style

	def get_size(self):
		return self.size

	def get_pattern(self):
		return self.pattern

	def get_color(self):
		return self.color

	def get_sbcatalog(self):
		return self.sbcatalog

	def get_upc(self):
		return self.upc

	def get_fsishort(self):
		return self.fsishort

	def get_fsilong(self):
		return self.fsilong

	def get_description(self):
		return self.description

	def get_qty(self):
		return self.qty_available

	def get_price(self):
		return self.price

	def set_price(self, price: float):
		self.price = price

	def set_style(self, style: str):
		self.style = style

	def set_category(self, category: str):
		self.category = category

	def set_qty_available(self, qty_available: int):
		self.qty_available = qty_available

	def set_pattern(self, pattern: str):
		self.pattern = pattern

	def set_fsishort(self, fsishort: str):
		self.fsishort = fsishort

	def set_fsilong(self, fsilong: str):
		self.fsilong = fsilong

	def set_description(self, description: str):
		self.description = description

	def set_size(self, size: str):
		self.size = size

	def set_color(self, color: str):
		self.color = color

	def set_upc(self, upc: str):
		self.upc = upc

	def set_status(self, status: bool):
		if status:
			self.status = 'Active'
		else:
			self.status = 'Inactive'

	def set_sbcatalog(self, sbcatalog: str):
		self.sbcatalog = sbcatalog

	def __str__(self):
		padding = 30
		header = ["|FSI Short#|", "|FSI Long#|", "|Style|", "|Pattern|", "|Description|", "|Size|", "|Color|", "|UPC|", "|Category|", "|Status|", "|SB-Style|", "|Qty Available|", "|Price|"]
		values = [self.fsishort, self.fsilong, self.style, self.pattern, self.description, self.size, self.color, self.upc, self.category, self.status, self.sbcatalog, self.qty_available, str(self.price)]
		hstring = ''
		vstring = ''

		for counter in range(0, len(header)):
			h = header[counter]
			v = values[counter]
			if counter == any({0, 1, 2, 3, 6}):
				hstring += h.ljust(int(padding * 0.75), ' ')
				vstring += v.ljust(int(padding * 0.75), ' ')
			elif counter == 4:
				hstring += h.ljust(int(padding * 2), ' ')
				vstring += v.ljust(int(padding * 2), ' ')
			else:
				hstring += h.ljust(padding, ' ')
				vstring += v.ljust(padding, ' ')

		return hstring + '\n' + vstring + '\n'

