import urllib.request
import re
import os

from modules.TemplateModule import TemplateModule

class Youtube(TemplateModule):
    def __init__(self, settings):
        TemplateModule.__init__(self, "Youtube")
        self.__url = settings["url"]
        self.__subscribers = 0
        self.check_data()

    def render(self, device):
        device.display_text(
            f"{self.__subscribers} abonnés",
            (120, 20, 20),
            (45, 45, 45),
            self.default_icon(),
        )
        return True

    def default_icon(self):
        return os.path.join(os.path.dirname(__file__), "src/youtube.png")

    def check_data(self):
        try:
            page = urllib.request.urlopen(self.__url).read()
            string_subs = re.findall(r"[0-9]*\sabonnés", page.decode("utf-8"))
            self.__subscribers = re.findall(r"[0-9]+", string_subs[0])[0]
        except:
            raise BaseException("error check_views()")
