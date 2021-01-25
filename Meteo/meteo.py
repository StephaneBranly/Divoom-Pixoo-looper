from bs4 import BeautifulSoup
import urllib.request
import re
import os
from PIL import Image, ImageDraw, ImageFont

class Meteo:
    def __init__(self):
        print("init")

    def updateImage(self):
        print("update image")
        im = Image.new(mode='RGB',size=(16,16))    
        
        iconIm = Image.open(os.path.join(os.path.dirname(__file__),"./icons/soleil.png"))
        im.paste(iconIm, (0,0),  iconIm.convert('RGBA'))
        imDraw = ImageDraw.Draw(im)           
        im.save(os.path.join(os.path.dirname(__file__),"./meteo.png"))

    def getMeteoImage(self):
        return os.path.join(os.path.dirname(__file__),"./meteo.png")
       