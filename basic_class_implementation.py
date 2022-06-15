class Car:
    def __init__(self,brand,color,type):
        self.brand = brand
        self.color = color
        self.type = type

    def drive(self):
    
        print(self.brand,"is driving")

    def stop(self):
        print(self.brand,"has stopped")


car1 = Car("tata","black","sports")
print(car1.brand)
print(car1.color)
print(car1.type)

car1.drive()

car1.stop()