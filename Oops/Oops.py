#object oriented programming in python

class family:
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def show(self):
		print(f"i am {self.name}")
		print(f"i am {self.age} years old")


class dog(family):

	def __init__(self,name,age,color):
		super().__init__(name,age)
		self.color = color

	def show(self):
		print(f"i am {self.name}")
		print(f"i am {self.age} years old and i am {self.color}")


f = family("rsk",40)
f.show()
d = dog("anitha",33,"black")
d.show()
