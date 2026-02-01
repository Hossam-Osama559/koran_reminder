from collections import defaultdict
from datetime import datetime,time 
from timerfd_creator import timerfd
from today_matches.today_matches import getting_the_matches
from alert.alert import alert_handler


class timerfd_and_match_mapping:


    def __init__(self):


        self.mapping=defaultdict(int)
    

    def __setitem__(self, name, value):
        
        self.mapping[name]=value
    

    def __getitem__(self, name):
        
        return self.mapping[name]


