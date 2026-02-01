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


class fd_handler:


    mapping_obj=timerfd_and_match_mapping()

    def __init__(self):



        ...

    # only special fd 
    @classmethod
    def fired_special_fd_handler(cls,fd,eventloop):


        matches,state=getting_the_matches.get_matches(eventloop)


        alert_handler.alert(matches)


        


    
    # normal fd 
    @classmethod
    def fired_normal_fd_handler(cls,fd):

        match=cls.mapping_obj[fd]

        # delegating the sending to another object 

        alert_handler.alert(match)
    

    @classmethod
    def new_fd(cls,match,fire_time,interval):

        # print(fire_time.split(":"))

        hours,minuts=map(int,fire_time.split(":"))

        target_time=time(hour=hours,minute=minuts)

        complete_target_date=datetime.combine(datetime.now().date(),target_time)

        delta=complete_target_date-datetime.now()

        seconds_till_target=int(delta.total_seconds())

        fd=timerfd.create_timerfd(seconds_till_target,interval)

        cls.mapping_obj[fd]=match

        return fd 

    