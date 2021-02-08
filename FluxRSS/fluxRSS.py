import feedparser
import os

class fluxRSS:
    def __init__(self, url):
        self.url = url
        self.news_feed=None
        self.updateNews()

    def updateNews(self):
        self.news_feed = feedparser.parse(self.url)

    def defaultIcon(self):
        return os.path.join(os.path.dirname(__file__),"./rss.png")

    def generateText(self,limit=5):
        cpt=0
        render=""
        for entry in self.news_feed.entries:
            if(cpt<limit):
                render=render+entry.title+" | "
            cpt=cpt+1
        return render.encode('cp1252').decode('latin-1')