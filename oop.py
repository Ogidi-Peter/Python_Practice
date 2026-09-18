class Dog:
    def __init__(self,name,breed):
            self.name = name
            self.breed = breed
    def bark(self):
        print("Bark")
    
        
dog1 = Dog("Savata","Eskimo")
dog1.bark()
print(dog1.name)
print(dog1.breed)


dog2 = Dog("Lala","German_Shephard")
dog2.bark()
print(dog2.name)
print(dog2.breed)

