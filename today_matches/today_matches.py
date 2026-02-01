from translator.team_names_translator import team_name_translator
from datetime import datetime ,time 
import requests
from bs4 import BeautifulSoup
import select


def getting_the_fdhandler_module():
    """importing the module in a function to prevent importing from partialy excuted module"""
    global fd_handler

    from eventloop.fd_handler import fd_handler
