class NewClass:
	def __init__(self):
		self.snails = sorted(["True", "True Blue", "White Mountainous Terrain"], key=len, reverse=True)
		for s in self.snails:
			print(s)
