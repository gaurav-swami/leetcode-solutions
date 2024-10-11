class Car:
	total_car = 0

	def __init__(self,brand,model):
		self.__brand = brand
		self.__model = model
		Car.total_car+=1

	def get_brand(self):
		return self.__brand

	def full_name(self):
		return f"{self.__brand} {self.__model}"

	def fuel_type(self):
		return "petrol or diesal"

	@staticmethod
	def general_description():
		return "cars are means of transport"

	@property
	def get_model(self):
		return self.__model

class ElectricCar(Car):
	def __init__(self, brand,model,battery_size):
		super().__init__(brand,model)
		self.battery_size = battery_size


	def full_name(self):
		return f"{self.brand} {self.model} "

	def fuel_type(self):
		return "electricity"

car_2 = ElectricCar("Tata","Nexon",10)
car_1 = Car("Tata","Nexon")




# print(car_2.__brand)
#print(car_2.fuel_type())
#print(car_1.fuel_type())
#print(Car.general_description())


print(car_2.get_model)
		