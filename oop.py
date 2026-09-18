########## Class Section ##########
class Dog:
    def __init__(self,name,breed,owner):
            self.name = name
            self.breed = breed
            self.owner = owner
    def bark(self):
        print("Bark")
    
class Owner:
    def __inti__(self,name,address,contact_no):
        self.name = name
        self.address = address
        self.contact_no = contact_no




######### Main Code #########
owner1 = Owner('Johnson','5,jj street','9045384538')
dog1 = Dog("Savata","Eskimo",owner1)
dog1.bark()
print(dog1.name)
print(dog1.breed)

owner1 = Owner('Danny','4,red street','9045584558')
dog2 = Dog("Lala","German Shephard")
dog2.bark()
print(dog2.name)
print(dog2.breed)

