class Vehicle:
    def __init__(self,Make:str,Model:str):
        self.Make = Make
        self.Model = Model
        
    def Move(self):
        print("Move along...")
        
class Airplane(Vehicle):
    def __init__(self,Make,Model,Id:str):
        super().__init__(Make,Model)
        self.Id = Id
    
        
my_Car = Vehicle("Ferrari","Model")
print(my_Car.Make)
my_Car.Move()

Plane =Airplane("boeing","747","N-453A")
print(Plane.Id)
