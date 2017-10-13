# construct the tweet object
# A tweet contains the username of user tweeting, a message, an optional picture, date and time of the tweet, and a list of comments 
# A tweet can take in comments


from datetime import datetime

class Tweet:

    def __init__(self,username,message,picture=None,date_time=datetime.now(),comments=[]):

        self.username = username
        self.message = message
        self.picture = picture
        self.date_time = date_time
        self.comments = []

    def add_comment(self,comment):
        self.comments.append(comment)