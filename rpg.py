class Role:
	def __init__(self, name, level, blood):
		self.name = name
		self.level = level
		self.blood = blood

	def __str__(self):
		return "('{name}', '{level}', '{blood}')".format(**vars(self))

	def __repr__(self):
		return self.__str__()

class SwordsMan(Role):
	def fight(self):
		print('sword fight...')
	
class Magician(Role):
	def fight(self):
		print('magic fight')
	def cure(self):
		print('magic cure')
