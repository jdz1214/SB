from Item import Item


def load_spreadsheet(spreadsheet):
	lines = []

	with open(spreadsheet, 'r') as f:
		fin = f.readlines()
		f.close()

	for counter in range(1, len(fin)):
		line = fin[counter]
		line = line.strip()
		lines.append(line.split('\t'))

	return lines


def load_fsi(fsi_lines):
	fsi_items = []
	# fsi_lines[0]: Short Item Number
	# fsi_lines[1]: Long Item Number
	# fsi_lines[2]: Description
	# fsi_lines[3]: Size
	# fsi_lines[4]: Color
	# fsi_lines[5]: UPC
	# fsi_lines[6]: Category
	# fsi_lines[7]: Status
	# fsi_lines[8]: Qty O/H
	# fsi_lines[9]: Qty Committed
	# fsi_lines[10]: Qty Available
	# fsi_lines[11]: Qty B/O
	# fsi_lines[12]: Reorder Point
	# fsi_lines[13]: 30-Day Usage
	# fsi_lines[14]: 60-Day Usage
	# fsi_lines[15]: 90-Day Usage
	# fsi_lines[16]: YTD Usage
	# Item(fsishort, fsilong, name, description, size, color, upc, category, status, sbstyle, pattern, qty_available, price)
	for line in fsi_lines:
		fsi_items.append(Item(line[0], line[1], line[2], line[5], line[6], line[7], '', line[10], 0.00))
	return fsi_items


def load_tops(office_tops_lines):
	office_tops = []
	# Style(Name), Color, XS, S, M, L, XL, XXL, UPC
	name = ''
	for t in office_tops_lines:
		top = t[0].split(',')
		if top[0] != '':
			name = str(top[0]).replace('The ', '')
		color = top[1]
		for col in range(2, 8):
			size = ''
			if col == 2:
				size = 'XS'
			elif col == 3:
				size = 'S'
			elif col == 4:
				size = 'M'
			elif col == 5:
				size = 'L'
			elif col == 6:
				size = 'XL'
			elif col == 7:
				size = 'XXL'
			description = ' '.join([name, color, size])
			office_tops.append(Item('', '', description, '', 'Tops', 'Active', '', top[col], 0.00))
	return office_tops


def load_boys(office_boys_lines):
	office_boys = []
	name = ''
	for b in office_boys_lines:
		boy = b[0].split(',')
		if boy[0] != '':
			name = str(boy[0]).replace('The ', '')
		color = boy[1]
		for col in range(2, 7):
			size = ''
			if col == 2:
				size = '4'
			elif col == 3:
				size = '6'
			elif col == 4:
				size = '8'
			elif col == 5:
				size = '10'
			elif col == 6:
				size = '12'
			description = ' '.join([name, color, size])
			office_boys.append(Item('', '', description, '', 'Boys', 'Active', '', boy[col], 0.00))
	return office_boys


def load_bottoms(office_bottoms_lines):
	office_bottoms = []
	name = ''
	for ob in office_bottoms_lines:
		bot = ob[0].split(',')
		if bot[0] != '':
			name = bot[0]
		color = bot[1]
		for col in range(2, 9):
			size = ''
			if col == 2:
				size = '30'
			elif col == 3:
				size = '32'
			elif col == 4:
				size = '34'
			elif col == 5:
				size = '36'
			elif col == 6:
				size = '38'
			elif col == 7:
				size = '40'
			elif col == 8:
				size = '42'
			description = ' '.join([name, color, size])
			office_bottoms.append(Item('', '', description, '', 'Bottoms', 'Active', '', bot[col], 0.00))
	return office_bottoms


def load_boardshorts(office_boardshorts_lines):
	office_boardshorts = []
	name = ''
	for bs in office_boardshorts_lines:
		board = bs[0].split(',')
		if board[0] != '':
			name = str(board[0]).replace('The ', '')
		color = board[1]
		for col in range(2, 9):
			size = ''
			if col == 2:
				size = '30'
			elif col == 3:
				size = '32'
			elif col == 4:
				size = '34'
			elif col == 5:
				size = '36'
			elif col == 6:
				size = '38'
			elif col == 7:
				size = '40'
			elif col == 8:
				size = '42'
			description = ' '.join([name, color, size])
			office_boardshorts.append(Item('', '', description, '', 'Boardshorts', 'Active', '', board[col], 0.00))
	return office_boardshorts


def load_swimtrunks(office_swimtrunks_lines):
	office_swimtrunks = []
	name = ''
	for st in office_swimtrunks_lines:
		swimtrunk = st[0].split(',')
		if swimtrunk[0] != '':
			name = str(swimtrunk[0]).replace('The ', '')
		color = swimtrunk[1]
		for col in range(2, 8):
			size = ''
			if col == 2:
				size = 'XS'
			elif col == 3:
				size = 'S'
			elif col == 4:
				size = 'M'
			elif col == 5:
				size = 'L'
			elif col == 6:
				size = 'XL'
			elif col == 7:
				size = 'XXL'
			description = ' '.join([name, color, size])
			office_swimtrunks.append(Item('', '', description, '', 'Swimtrunks', 'Active', '', swimtrunk[col], 0.00))
	return office_swimtrunks


def reconcile_fsi_with_office(fsi_items: list, office_items: list):
	# if name, size, color, category match, then add information.
	# fsi_items are missing 1) sbstyle
	# office_items are missing 1) upc
	for oi in office_items:
		for fsi in fsi_items:
			if fsi.get_style() == oi.get_style() and fsi.get_color() == oi.get_color() and fsi.get_size() == oi.get_size():
				oi.set_upc(fsi.get_upc())
				oi.set_fsishort(fsi.get_fsishort())
				oi.set_fsilong(fsi.get_fsilong())
	return office_items
