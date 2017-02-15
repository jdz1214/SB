import csv


def show_reorder(items: list, fsi_items: list):
	reorders = []
	for item in items:
		for fsi in fsi_items:
			if item.get_style() == fsi.get_style() and item.get_size() == fsi.get_size() and item.get_color() == fsi.get_color() and item.get_category() == fsi.get_category() and int(fsi.get_qty()) < 15:
				reorders.append(fsi)
	#  reorders = [item for item in items if item.get_upc() and int(item.get_qty()) < 15 and item.get_size() != 'XS']
	reorders.sort(key=lambda item: int(item.get_qty()))
	with open(r'/Users/jdz/PycharmProjects/StrongBoalt/resources/reorders.csv', 'w', newline='') as csvfile:
		reorderwriter = csv.writer(csvfile, dialect='excel', delimiter=',')
		reorderwriter.writerow(['Reorder Qty', 'Name', 'Size', 'Color', 'Pattern', 'UPC'])
		for item in reorders:
			reorderwriter.writerow([(15 - int(item.get_qty())), item.get_style(), item.get_size(), item.get_color(), item.get_pattern(), item.get_upc()])
		csvfile.close()
	print('Total number of items to order: ', sum((15 - int(item.get_qty())) for item in reorders))
	print('Number of items in reorder list: ', len(reorders))
	print('Total preexisting qty: ', sum(int(item.get_qty()) for item in reorders))
	return [item for item in items if int(item.get_qty()) < 15]

