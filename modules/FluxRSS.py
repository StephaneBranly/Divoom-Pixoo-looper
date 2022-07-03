import os
import feedparser

from modules.TemplateModule import TemplateModule


class FluxRSS(TemplateModule):
    def __init__(self, settings):
        TemplateModule.__init__(self, "FluxRSS")
        self.__url = settings["url"]
        self.__news_feed = None
        self.update_news()

    def render(self, device):
        device.display_text(
            f"Actu: {self.generate_text(1)}",
            (170, 00, 235),
            (0, 110, 110),
            self.default_icon(),
        )
        return True

    def update_news(self):
        self.__news_feed = feedparser.parse(self.__url)

    def default_icon(self):
        return os.path.join(os.path.dirname(__file__), "src/rss.png")

    def generate_text(self, limit=5):
        cpt = 0
        render = ""
        for entry in self.__news_feed.entries:
            if cpt < limit:
                render = render + entry.title + " | "
            cpt = cpt + 1
        return render.encode("cp1252").decode("latin-1")
