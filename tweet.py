from datetime import datetime

class Tweet:

    def __init__(self,message,date_time,username,comments):

        self.username = username
        self.message = message
        self.date_time = datetime.now()
        self.comments = []

    def add_comment(self,comment):
        self.comments.append(comment)


class TweetPic:

    def _init__(self,picture,caption,date_time,username,comments):
        self.username = username
        self.picture = picture
        self.caption = caption
        self.date_time = datetime.now()
        self.comments = []

    def add_comment(self,comment):
        self.comments.append(comment)


class RetweetTweet:

    def __init__(self,new_message,message,username,retweet_time,comments):

        self.username = username
        self.new_message = new_message
        self.retweet_time = retweet_time
        self.comments = []

    def add_comment(self,comment):
        self.comments.append(comment)

class RetweetPic:

    def __init__(self,new_message,picture,caption,username,retweet_time,comments):

        self.username = username
        self.new_message = new_message
        self.retweet_time = retweet_time
        self.comments = []

    def add_comment(self,comment):
        self.comments.append(comment)