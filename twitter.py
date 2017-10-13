# The twitter class contains users a list of users who have signed up and an istance of the signedin user.
# this module can signup users an, sign them in and out

import user as usr
print(usr.User)
import tweet
import comments


class Twitter:

    def __init__(self):
        self.logged_in = None
        self.user_list = []

    def sign_up(self,user):
        self.user_list.append(user)

    def sign_in(self,user):
        self.logged_in = user

    def sign_out(self):
        self.logged_in = None

    def find_user(self, name_or_email):
        for user in self.user_list:
            if user.username == name_or_email or user.email == name_or_email:
                return user
        
        return None

def main():

    main_loop = True

    while main_loop:

        print("Welcome The Twitter Clone")

        twit = Twitter()
        option = int(input("1 New to twitter? Sign Up\n2 Already have an account? Log In\n"))

        if option == 1:#sign up sequence
                
            print("Welcome to twitter!\nJust a few details and we\'re done :)\n")
            
            name_ = input("Enter your name: ")
            username_ = input("Enter a username: ")
            email_ = input("Enter an email address: ")
            password_ = input("Enter a password: ")

            twit.sign_up(usr.User(name_, username_, email_, password_))

        elif option == 2:#Log in sequence
            print("Welcome Back")

            name_ = input("Enter your username or email: ")
            password_ = input("Enter password: ")

            my_user = twit.find_user(name_)

            if my_user:
                if my_user.password == password_:
                    twit.sign_in(user)
                    print("You are now logged in")

                    home = int(input("1 Tweet\n2 Retweet\n3 View Profile\n4 Log out\n\n"))

                    for user in twit.user_list:#Get tweets
                        user.get_tweets

                    if home == 1:
                        
                        tweet_type = int(input("\n1 Text or\n2 Picture\n"))
                        
                        if tweet_type == 1:

                            tweet_prompt = input("Type your tweet here: \n")
                            
                            if len(tweet_prompt) <= 280 and len(tweet_prompt) > 0:
                                tweet_username_ = twit.logged_in.username
                                tweet_message_ = tweet_prompt

                                tweet_ = tweet.Tweet(tweet_username_,tweet_message_)
                                twit.logged_in.tweet_action(tweet_)

                            else:
                                print("Your tweet is too long...")
                    
                    elif tweet_type == 2:

                        pass

            else:
                print("Wrong username or password")




            # for user in twit.user_list:
                
            #     if user.password == password_ and (user.username == name_ or user.email == name_):
                
            #         twit.sign_in(user)
            #         print("You are now logged in")

            #         twit = Twitter()
            #         home = int(input("1 Tweet\n2 Retweet\n3 View Profile\n4 Log out\n\n"))

            #         for user in twit.user_list:#Get tweets
            #             user.get_tweets

            #         if home == 1:
                        
            #             tweet_type = int(input("\n1 Text or\n2 Picture\n"))
                        
            #             if tweet_type == 1:

            #                 tweet_prompt = input("Type your tweet here: \n")
                            
            #                 if len(tweet_prompt) <= 280 and len(tweet_prompt) > 0:
            #                     tweet_username_ = twit.logged_in.username
            #                     tweet_message_ = tweet_prompt

            #                     tweet_ = tweet.Tweet(tweet_username_,tweet_message_)
            #                     twit.logged_in.tweet_action(tweet_)

            #                 else:
            #                     print("Your tweet is too long...")
                    
            #         elif tweet_type == 2:

            #             pass
                
            #     else:
            #         print("Wrong username or email!\nTry Again.")

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()