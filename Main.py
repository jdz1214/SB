from Item import Item
import Utilities


def main():
	execute()


def execute():
	items = load(r'/Users/jdz/Google Drive/Business/Strong Boalt/InventoryInquiryReport.csv')
	items.sort(key=lambda i: i.get_qty() == '0')
	for item in items:
		print(item)


def load(fsi_spreadsheet):  # office_spreadsheet
	items = []
	fsi_lines = Utilities.load_spreadsheet(fsi_spreadsheet)
	# office_lines = Utilities.load_spreadsheet(office_spreadsheet)
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
	# office_lines[0]:

	for line in fsi_lines:
		items.append(Item(line[0], line[1], line[2], line[5], line[6], line[7],
		                  'sbstyle', line[10], 0.00))

	return items




main()
