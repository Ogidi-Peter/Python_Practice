class User:
    def __init__(self,username,email,password):
        self.username = username
        self._email = email
        self.password = password
        
   ##Getter property##
    @property
    def email(self):
        print("Email accessed")
        return self._email  

user1 = User("Danny","dan@gmail.com","1212dr")

print(user1.email)