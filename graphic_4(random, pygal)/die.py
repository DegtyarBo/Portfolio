from random import randint

class Die():
	'''Класс пердставляющий один кубик'''
	def __init__(self, num_sides = 6):
		'''по умолчанию шестигранный кубик'''
		self.num_sides = num_sides
		
	def roll(self):
		'''возвращает случайное число от 1 до числа граней'''
		return randint(1, self.num_sides)
