class User:
    User_count = 0
    
    def __init__(self,username,email):
        self.username = username
        self.email = email
        User.User_count +=1
        
    def display(self):
        print(f"Username: {self.username}, Email: {self.email}")
        
user1 = User('Danny','Dan@gmail.com')
user2 = User('May','may@gmail.com')

print(User.User_count)
print(user1.User_count)
print(user2.User_count)