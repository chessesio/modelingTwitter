# construct user object
# user has a [name, username, email, password]<-- must have, profile picture and tweers[]
# user can tweet or retweet

class User:

    def __init__(self,name,username,email,password):

        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.prof_pic = "upload a picture"
        self.tweets = []

#   user tweeting action
    def tweet_action(self,new_tweet):
        self.tweets.append(new_tweet)

#   user can retweet
    def retweet_action(self,a_retweet):
        self.tweets.append(a_retweet)

#   display a users tweets
    def get_tweets(self):
        for tweet in self.tweets:
            print(tweet)