class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0


	def get_descriptive_name(self):
		long_name = str(self.year)+' '+self.model+' '+self.make
		return long_name.title()

	def update(self,mileage):
		
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print "You can not roll back an odometer."

	def increment(self,mileage):
		self.update += mileage

	
	def read_odometer(self):
		print "This car has "+str(self.odometer_reading)+" miles on it."

class ElectricCar(Car):
	def car(self, make, model, year):
		super(ElectricCar, self).car(make, model, year)

my_car = ElectricCar('audi','a4',2017)
print my_car.make+' '+my_car.model+' '+str(my_car.year)
# my_car.update(30)
# my_car.read_odometer()
