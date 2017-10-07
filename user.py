class User:

    def __init__(self,name,username,email,password):

        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.prof_pic = ""
        self.tweets = []

    def tweet_action(self,a_tweet):
        self.tweets.append(a_tweet)

    def retweet_action(self,a_retweet):
        self.tweets.append(a_retweet)