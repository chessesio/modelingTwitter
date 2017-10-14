# The twitter class contains users a list of users who have signed up and an istance of the signedin user.
# this module can signup users an, sign them in and out

import user as usr
import tweet
import comments
import csv
import os

class Twitter:

    def __init__(self):
        self.logged_in = None
        # self.user_list = []

    def sign_up(self,name_,username_,email_,password_,profile_pic_):
        file_exist = os.path.isfile("users.csv")

        with open("users.csv","a") as userlist:

            fieldnames = ["name", "username","email","password","profile picture"]

            writer = csv.DictWriter(userlist,fieldnames=fieldnames)

            if not file_exist:
                writer.writeheader()
            
            writer.writerow({"name":name_,"username":username_,"email":email_,"password":password_,"profile picture":profile_pic_})

        # self.user_list.append(user)

    def sign_in(self,user_):
        # name,username,email,password
        # self.logged_in = user.User(name=user_.get("name"),username=user_.get("username"),email=user_.get("email"),password=user_.password)
        self.logged_in = user_

    def sign_out(self):
        self.logged_in = None

    def find_user(self, name_or_email):
        print(self.user_list)
        for user_ in self.user_list:

            if user_.username == name_or_email:
                return user_
        return False

twit = Twitter()

def main():
    loop = True
    while loop:
        print("Welcome The Twitter Clone")

        option = int(input("1 New to twitter? Sign Up\n2 Already have an account? Log In\n"))

        if option == 1:#sign up sequence

            print("Welcome to twitter!\nJust a few details and we\'re done :)\n")
            
            name_ = input("Enter your name: ")
            username_ = input("Enter a username: ")
            email_ = input("Enter an email address: ")
            password_ = input("Enter a password: ")
            profile_pic_ = None

            twit.sign_up(name_, username_, email_, password_,profile_pic_)
            # print(twit.user_list)

        elif option == 2:#Log in sequence
            print("\nWelcome Back\n")

            name_ = input("Enter your username or email: ")
            password_ = input("Enter password: ")

            with open("users.csv","r") as userlist:
                reader = csv.DictReader(userlist)
                for row in reader:
                    if (name_ == row.get("username") or name_ == row.get("email")) and password_ == row.get("password"):
                        name_ = row.get("name")
                        username_ = row.get("username")
                        email_ = row.get("email")
                        password_ = row.get("password")
                        profile_pic_ = row.get("profile picture")
                        
                        twit.sign_in(usr.User(name_,username_,email_,password_))
                        
                        home()

                    else:
                        print("Wrong Username/email or password")

                # my_user = twit.find_user(name_)
                # if my_user:
                #     if my_user.password == password_:
                #         twit.sign_in(my_user)
                #         print("\nYou are now logged in\n")
                #         home()


                # else:
                #     print("Wrong username or password")

        else:
            print("Invalid option")


# home function to be called after sign up
def home():
    home_ = int(input("1 Tweet\n2 View Profile\n3 Log out\n\n"))

    twit.logged_in.get_tweets()

    if home_ == 1:

        tweet_type = int(input("\n1 Text or\n2 Picture\n"))
        
        if tweet_type == 1:

            tweet_prompt = input("Type your tweet here: \n")
            
            if len(tweet_prompt) <= 280 and len(tweet_prompt) > 0:
                #Take user's username
                #Take the tweet message
                #Append to uer's tweets list
                
                tweet_username_ = twit.logged_in.username
                new_tweet = tweet.Tweet(tweet_username_,tweet_prompt)

                twit.logged_in.tweet_action(new_tweet)

            else:
                print("Your tweet is too long...")

        elif tweet_type == 2:

                tweet_prompt = input("\nType your tweet here: \n")
                picture_ = input("Upload picture:\n\n")

                if len(tweet_prompt) <= 280 and len(tweet_prompt) > 0:
                    #Take user's username
                    #Take the tweet message
                    #Append to uer's tweets list
                    
                    tweet_username_ = twit.logged_in.username

                    new_tweet = tweet.Tweet(username=tweet_username_,message=tweet_prompt,picture=picture_)

                    twit.logged_in.tweet_action(new_tweet)

                else:
                    print("Your tweet is too long...")
    
    elif home_ == 2:
        profile()

    elif home_ == 3:
        twit.logged_in = None
        

    else:
        print("Invalid choice")

def profile():
    print("Name: {}\nUsername: {}\nProfile Picture: {}\n".format(twit.logged_in.name,twit.logged_in.username,twit.logged_in.prof_pic))

    twit.logged_in.get_tweets()

    go_home = input("1. Home")
    if go_home == "1":
        home()

if __name__ == "__main__":
    main()