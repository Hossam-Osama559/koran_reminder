import os 
import sys 
from eventloop import event_loop
from eventloop.fd_handler import fd_handler
import select 
import special_fd 



class runner:


    def __init__(self):

        # there will be 2 types of fd's 
        # 1--the special one which will only exist one of it and this will run every day at 12pm getting the whole day matches 
        # 2--the normal ones and those will be there a one for each match that will be fired in the date of this match only
        global special_fd

        self.special_fd=fd_handler.new_fd("special","1:23",24*3600)

        
        special_fd.special_fd=self.special_fd


        

        

        self.event_loop=event_loop.eventloop()

    

    def run(self):


        # self.set_process_as_daemon()




        self.event_loop.register_fd(self.special_fd,select.EPOLLIN)


        self.event_loop.run()



    def set_process_as_daemon(self):


        pid=os.fork()

        if pid:

            os._exit(0)

        

        os.setsid()


        pid=os.fork()

        if pid:

            os._exit(0)

        

        os.chdir("/")

        os.umask(0)


        sys.stderr.flush()
        sys.stdout.flush()



        with open("/dev/null","rb") as inp_fd:

            os.dup2(inp_fd.fileno(),sys.stdin.fileno())

        
        with open("/dev/null","ab") as out_fd:

            os.dup2(out_fd.fileno(),sys.stdout.fileno())
            os.dup2(out_fd.fileno(),sys.stderr.fileno())



