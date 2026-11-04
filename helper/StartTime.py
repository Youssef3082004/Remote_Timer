from datetime import datetime

class Time:

    @staticmethod
    def get_current_time():
        return datetime.now().strftime(format="%I:%M %p") 
    