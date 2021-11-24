class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username  # Self Is to identify that Every attribute passed in a constructur is belong ing of class itself.
        self.followers = 0  # //default value need not to be passed during object creation.
        self.following = 0

    def follow(self, user): # these Class object (user_1) follows to another class object(User_2)
        user.followers += 1 # user_2 followers increased by 1
        self.following += 1 # user_1(self) following  increased by 1


User_1 = User(3, "Shubham")#objects created of user_1 and User_2
User_2 = User(6,"Vivek")

User_1.follow(User_2) #User_1 calling follow function to follow User_2 by pasiing user_2
print(User_1.following)#Acessing attributes of User_1
print(User_2.followers)#Acessing attributes of User_2

