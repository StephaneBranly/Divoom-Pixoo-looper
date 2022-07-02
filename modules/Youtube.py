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
        device.displayText(
            f"@stephane_branly : {self.__subscribers} abonnés",
            (120, 20, 20),
            (45, 45, 45),
            self.default_icon(),
        )

    def default_icon(self):
        return os.path.join(os.path.dirname(__file__), "src/yt.png")

    def check_data(self):
        try:
            page = urllib.request.urlopen(self.__url).read()
            string_subs = re.findall(r"[0-9]*\sabonnés", page.decode("utf-8"))
            self.__subscribers = re.findall(r"[0-9]+", string_subs[0])[0]
        except:
            raise "error check_views()"
