import datetime

class Person:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age

	def show(self):
		print(f'{self.name} is {self.height} is {self.age}')

	@classmethod
	def from_birth(cls, name, height, age):
		return cls(name, height, datetime.datetime.now().year - age)


p = Person.from_birth('amir', 180, 1990)
p.show()