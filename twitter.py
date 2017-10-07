import user
import tweet
import comments

logged_in = None

class Twitter(user.User):

    def __init__(self):
        self.user_list = []

    def add_user(self,user):
        self.user_list.append(user)

    def sign_up(self):
        
        print("Welcome to twitter!\nJust a few details and we\'re done :)\n")
        
        name_ = input("Enter your name: ")
        username_ = input("Enter a username: ")
        email_ = input("Enter an email address: ")
        password_ = input("Enter a password: ")
        
        new_user = super().__init__(name=name_,username=username_,email=email_,password=password_)

        self.add_user(new_user)

    def sign_in(self):

        print("Welcome Back")

        name_ = input("Enter your username or email")

        for user in self.user_list:
            if user.username == name_ or user.email == name_:
                logged_in_user = user
                print("You are now logged in")
                return user

            else:
                print("Wrong username or email!\nTry Again.")

    def sign_out(self):
        logged_in_user = None

    def text_tweet()

i = Twitter()
i.sign_up()
print(len(i.user_list))