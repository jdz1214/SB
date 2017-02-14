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
