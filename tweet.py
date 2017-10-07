from datetime import datetime

class Tweet:

    def __init__(self,username,message,picture,date_time,comments):

        self.username = username
        self.message = message
        self.picture = None
        self.date_time = datetime.now()
        self.comments = []

    def add_comment(self,comment):
        self.comments.append(comment)