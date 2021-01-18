from bs4 import BeautifulSoup
import urllib.request
import re


class Youtube:
    def __init__(self, url):
        self.url = url
        self.subscribers = 0
        self.view = 0
    
    def check_views(self):
        try:
            page  = urllib.request.urlopen(self.url).read()
            string_subs = re.findall(r"[0-9]*\sabonnés", page.decode("utf-8")) 
            self.subscribers = re.findall(r'[0-9]+', string_subs[0])[0]
        except:
            print("error check_views()")