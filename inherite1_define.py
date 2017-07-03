class Person(object):
	"""docstring for Car"""
	def __init__(self, name,age,score):
		self.name = name
		self.age = age
		self.score = score

	def get_descriptive(self):
		print "My teacher's name is "+self.name.title()+"."
		print "My teacher's age is "+str(self.age)+"."
		print "My teacher's score is "+str(self.score)+"."

class Teacher(Person):

	def __init__(self,name, age, score,grade):
		super(Teacher, self).__init__(name,age,score)
		self.grade = grade

	def get_des(self):
		print "My teacher is teaching "+str(self.grade)+" grade."

# my_school = Teacher("allen",12,90,43)
# my_school.get_descriptive()
# my_school.get_des()