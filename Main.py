import Functions
import Utilities


def main():
	items = execute()
	path = r'/Users/jdz/Google Drive/Business/Strong Boalt/'
	fsi_items = Utilities.load_fsi(Utilities.load_spreadsheet(path + r'InventoryInquiryReport.csv'))
	reorders = Functions.show_reorder(items, fsi_items)


def execute():
	path = r'/Users/jdz/Google Drive/Business/Strong Boalt/'
	fsi_spreadsheet = path + r'InventoryInquiryReport.csv'
	office_tops = path + r'Office Tops.csv'
	office_boys = path + r'Office Boys.csv'
	office_bottoms = path + r'Office Bottoms.csv'
	office_boardshorts = path + r'Office Boardshorts.csv'
	office_swimtrunks = path + r'Office Swimtrunks.csv'
	items = load(fsi_spreadsheet, office_tops, office_boys, office_bottoms, office_boardshorts, office_swimtrunks)
	for item in items:
		if item.get_qty() == '':
			item.set_qty_available('0')
	return items


def load(fsi_spreadsheet, office_tops, office_boys, office_bottoms, office_boardshorts, office_swimtrunks):  # office_spreadsheet
	items = []
	fsi_lines = Utilities.load_spreadsheet(fsi_spreadsheet)
	office_tops_lines = Utilities.load_spreadsheet(office_tops)
	office_boys_lines = Utilities.load_spreadsheet(office_boys)
	office_bottoms_lines = Utilities.load_spreadsheet(office_bottoms)
	office_boardshorts_lines = Utilities.load_spreadsheet(office_boardshorts)
	office_swimtrunks_lines = Utilities.load_spreadsheet(office_swimtrunks)

	fsi_items = Utilities.load_fsi(fsi_lines)
	office_tops = Utilities.load_tops(office_tops_lines)
	office_boys = Utilities.load_boys(office_boys_lines)
	office_bottoms = Utilities.load_bottoms(office_bottoms_lines)
	office_boardshorts = Utilities.load_boardshorts(office_boardshorts_lines)
	office_swimtrunks = Utilities.load_swimtrunks(office_swimtrunks_lines)
	for ol in [office_tops, office_boys, office_bottoms, office_boardshorts, office_swimtrunks]:
		l = Utilities.reconcile_fsi_with_office(fsi_items, ol)
		for i in l:
			items.append(i)
	# for i in fsi_items:
	# 	items.append(i)
	return items


main()
