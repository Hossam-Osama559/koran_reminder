from collections import defaultdict
from deep_translator import GoogleTranslator





class cache_team_names:

    def __init__(self):

        self.cache=defaultdict(int)

    

    def get_name(self,name):


        if self.cache[name]!=0:

            return self.cache[name]
        
        else:
            return None
    

    def set_name(self,name,translated_name):

        self.cache[name]=translated_name




class team_name_translator:

    def __init__(self):

        self.name_cache=cache_team_names()

    
    def translate(self,team_name):


        # api call

        if self.name_cache.get_name(team_name) is None:

            trans=GoogleTranslator(source='ar',target='en').translate(f"{team_name}")

            self.name_cache.set_name(team_name,trans)

            return trans


        elif self.name_cache.get_name(team_name) is not None:

            return self.name_cache.get_name(team_name)