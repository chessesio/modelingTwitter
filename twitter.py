import user
import tweet
import comments


class Twitter(user.User,):

    def __init__(self):
        self.logged_in = None
        self.user_list = []

    def add_user(self,user):
        self.user_list.append(user)

    def sign_up(self, name_, username_, email_, password_):
        new_user = super().__init__(name=name_,username=username_,email=email_,password=password_)
        self.add_user(new_user)

    def sign_in(self,user):
        self.logged_in = user

    def sign_out(self):
        self.logged_in = None
        
def main():


    main_loop = 3

    while main_loop != 5:

        print("Welcome The Twitter Clone")

        twit = Twitter()
        option = int(input("1 New to twitter? Sign Up\n2 Already have an account? Log In\n"))

        if option == 1:
            print("Welcome to twitter!\nJust a few details and we\'re done :)\n")
            
            name_ = input("Enter your name: ")
            username_ = input("Enter a username: ")
            email_ = input("Enter an email address: ")
            password_ = input("Enter a password: ")

            twit.sign_up(name_, username_, email_, password_)
            
            

        if option == 2:
            print("Welcome Back")

            name_ = input("Enter your username or email: ")

            for user in twit.user_list:
                if user.username == name_ or user.email == name_ and :
                    twit.logged_in = user
                    print("You are now logged in")
                    return user
                    home()
            else:
                print("Wrong username or email!\nTry Again.")

def home():

    twit = Twitter()
    home = input("1 Tweet\n2 Retweet\n3 View Profile\n4 Log out\n\n")

    for user in twit.user_list:
        user.get_tweets








if __name__ == "__main__":
    main()