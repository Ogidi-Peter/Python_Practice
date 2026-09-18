class User:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
        
    def say_hi(self,user):
        print(f"Sending message to {user.username} Hi{user.username} it's {self.username}")
        
        
        
user1 = User('Danny','dan@gmail.com','123re')

print(user1.email)
user1.email='danny@gmail.com'

print(user1.email)