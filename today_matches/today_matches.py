from translator.team_names_translator import team_name_translator
from datetime import datetime ,time 
import requests
from bs4 import BeautifulSoup
import select


def getting_the_fdhandler_module():
    """importing the module in a function to prevent importing from partialy excuted module"""
    global fd_handler

    from eventloop.fd_handler import fd_handler









class url_generator:


    @classmethod
    def get_url(cls):


        date=datetime.now()


        url_date=f"{date.month}/{date.day}/{date.year}"

        url=f"https://www.yallakora.com/match-center?date={url_date}#days"


        return url 





class  getting_the_matches:
    
    translator=team_name_translator()



    def __init__(self):


        # self.url_provider=url_generator()

        # self.translator=team_name_translator()

        # self.file_decriptor_handler=fd_handler()
        ...

    @classmethod
    def get_matches(cls,eventloop):


        getting_the_fdhandler_module()


        # request call
        html = requests.get(url_generator.get_url()).text





        
        soup = BeautifulSoup(html, "html.parser")



        x =soup.find(class_="2968 matchCard matchesList")

        if x is not None:

            teams=zip(x.find_all(class_="teams teamA"),x.find_all(class_="teams teamB"),x.find_all(class_="time"))



            matches=""


            for teama,teamb,date in teams:
                match=(f"{cls.translator.translate(teama.text.strip('\n'))} vs {cls.translator.translate(teamb.text.strip('\n'))} at {(date.text.strip('\n'))}")

                matches+=match+'\n'

                # creating a normal fd for each match 
                fd=fd_handler.new_fd(match,date.text,0)


                eventloop.register_fd(fd,select.EPOLLIN)
            # 1 means that there is matches today 
            return matches,1



        elif x is None:

            matches="no matches today in the premier league "

            # zero means that there is no matches today 
            return matches,0
