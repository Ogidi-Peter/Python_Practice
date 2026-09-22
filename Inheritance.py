class Vehicle:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    
    def start(self):
        print("vehicle is starting")
        
    def stop(self):
        print("vehicle is stopping")
        
class Car(Vehicle):
    def __init__(self,brand,model,year,no_of_doors,no_of_wheels):
        
        super().__init__(brand,model,year)
        self.no_of_doors = no_of_doors
        self.no_of_wheels = no_of_wheels
        
class Bike(Vehicle):
    def __init__(self,brand,model,year,no_wheels):
        super().__init__(brand,model,year)
        self.no_wheels = no_wheels
        
        
car = Car("Lexus","EX-350",2026,4,4)
bike= Bike("Honda","Scoopy",2018,2)
print(car.__dict__)