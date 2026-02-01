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





