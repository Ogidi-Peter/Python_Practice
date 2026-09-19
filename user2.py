class User:
    def __init__(self,username,email,password):
        self.username = username
        self._email = email
        self.password = password
        
    def get_email(self):
        return self._email
    
    def set_email(self):
        self._email = new_email
        
user1 = User("Danny","dan12@gmail.com","123dr")

print(user1.get_email())

user1.set_email("danny@gmail.com")
print(user1.get_email())