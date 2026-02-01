import select
from .fd_handler import fd_handler
import os 
import special_fd 



class eventloop:


    def __init__(self):

        self.eventhandler=fd_handler()

        self.epoll_instance=select.epoll()




    def register_fd(self,fd,event):

        self.epoll_instance.register(fd,event)
    

    def run(self):

        while True:

            events=self.epoll_instance.poll()


            for fd,event in events:


                if fd==special_fd.special_fd:





                    _=os.read(fd,8)
                    
                    self.eventhandler.fired_special_fd_handler(fd,self)
                


                else:


                    _=os.read(fd,8)

                    self.eventhandler.fired_normal_fd_handler(fd)