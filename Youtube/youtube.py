from bs4 import BeautifulSoup
import urllib.request
import re
import os

class Youtube:
    def __init__(self, url):
        self.url = url
        self.subscribers = 0
        self.view = 0
        self.check_data()

    def defaultIcon(self):
        return os.path.join(os.path.dirname(__file__),"./yt.png")
    
    def check_data(self):
        try:
            page  = urllib.request.urlopen(self.url).read()
            string_subs = re.findall(r"[0-9]*\sabonnés", page.decode("utf-8")) 
            self.subscribers = re.findall(r'[0-9]+', string_subs[0])[0]
        except:
            print("error check_views()")