from bs4 import BeautifulSoup
import urllib.request
import re
import os
from PIL import Image, ImageDraw, ImageFont

class Meteo:
    def __init__(self, url):
        self.url = url
        self.temperature = '-10 °C'
        
    def update(self):
        print("update data :")
        page  = urllib.request.urlopen(self.url).read()

        table_meteo = re.findall(r"<table style=\"border-collapse: collapse;\" \s?border=1 \s?cellpadding=2 \s?cellspacing=0 \s?bordercolor=#a0a0b0\s?>.*</table>", page.decode("iso-8859-1")) 

        soup = BeautifulSoup(table_meteo[0],features="lxml")
        rows = soup.findAll('tr')
       
        row = self.soupLine(str(rows[2]))
        for td in row:
            print(td)

        self.temperature = re.findall(r"[0-9-]*\s°C", str(row[2]))[0]
        self.temperature = re.findall(r"[0-9-]*", str(self.temperature))[0]
        print(self.temperature)
        self.generateImage()
    
    def soupLine(self,line):
        soup = BeautifulSoup(line,features="lxml")
        cells = soup.findAll('td')
        return cells

    def generateImage(self):
        im = Image.new(mode='RGB',size=(16,16))    
        color1 = (9,99,235)
        color2 = (61,133,242)
        for i in range(16):
            current_color = (int(color1[0]+((color2[0]-color1[0])/16*i)),int(color1[1]+((color2[1]-color1[1])/16*i)),int(color1[2]+((color2[2]-color1[2])/16*i)))
            shape = [(0, i), (15, i)] 
            img1 = ImageDraw.Draw(im)   
            img1.line(shape, fill =current_color, width = 0) 
        # if icon:
        iconDeg = Image.open(os.path.join(os.path.dirname(__file__),"./icons/degC.png"))
        im.paste(iconDeg, (12,8),  iconDeg.convert('RGBA'))
        iconThermo = Image.open(os.path.join(os.path.dirname(__file__),"./icons/thermo.png"))
        im.paste(iconThermo, (1,8),  iconThermo.convert('RGBA'))
        font = ImageFont.truetype(os.path.join(os.path.dirname(__file__),"../src/pixelated.ttf"), size=8)
        imDraw = ImageDraw.Draw(im)  
        fontDeltaX = font.getsize(self.temperature)[0]+3
        imDraw.text((15 - fontDeltaX,7), self.temperature, (230, 230, 230),font=font)
        imDraw.text((15 - fontDeltaX,8), self.temperature, (50, 50, 50),font=font)
        # imDraw.text((1,3), self.temperature, (210, 200, 191), font=font)

        im.save(os.path.join(os.path.dirname(__file__),"./meteo.png"))  

    def getMeteoImage(self):
        return os.path.join(os.path.dirname(__file__),"./meteo.png")
       