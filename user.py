class User:
    def __init__(self,username,email,password):
        self.username = username
        self._email = email #Protected#
        self.password = password
        
    def clean_email(self):
        return self._email.lower().strip()
    
    def say_hi(self,user):
        print(f"Sending message to {user.username} Hi{user.username} it's {self.username}")
        
        
        
user1 = User('Danny','Dan@gmail.com','123re')

print(user1._email)
print(user1.clean_email())