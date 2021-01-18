import feedparser

class fluxRSS:
    def __init__(self, url):
        self.url = url
        self.news_feed=None

    def updateNews(self):
        self.news_feed = feedparser.parse(self.url)

    def generateText(self,limit=5):
        cpt=0
        render=""
        for entry in self.news_feed.entries:
            if(cpt<limit):
                render=render+entry.title+" ; "
            cpt=cpt+1
        print(render)
        return render.encode('utf-8').decode('latin-1')