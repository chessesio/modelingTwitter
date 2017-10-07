from datetime import datetime

class Comment:

    def __init__(self,message,date_time,username):
        self.username = username
        self.message = message
        self.date_time = datetime.now()