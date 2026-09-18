########## Class Section ##########
class Dog:
    def __init__(self,name,breed,owner):
            self.name = name
            self.breed = breed
            self.owner = owner
    def bark(self):
        print("Bark")
    
class Owner:
    def __init__(self,name,address,contact_no):
        self.name = name
        self.address = address
        self.contact_no = contact_no




######### Main Code #########

owner1 = Owner("Johnson","5 jj street","9045384538")
dog1 = Dog("dan","Eskimo",owner1)
print(dog1.owner.name)

owner2 = Owner("Danny","4,red street","9045584558")
dog2 = Dog("Lala","Greyhound",owner2)
print(dog2.owner.name)
