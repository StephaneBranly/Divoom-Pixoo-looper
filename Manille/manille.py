import re
import os
from PIL import Image, ImageDraw, ImageFont

class Manille:
    def __init__(self, color1, color2):
        self.sc_team1 = 0
        self.sc_team2 = 0
        self.cl_team1 = color1
        self.cl_team2 = color2
        
    def generateImage(self,score1=0,score2=0):
        im = Image.new(mode='RGB',size=(16,16))    
        color1 = self.cl_team1
        color2 = (1,1,1)
        for i in range(8):
            current_color = (int(color1[0]+((color2[0]-color1[0])/8*i)),int(color1[1]+((color2[1]-color1[1])/8*i)),int(color1[2]+((color2[2]-color1[2])/8*i)))
            shape = [(0, i), (15, i)] 
            img1 = ImageDraw.Draw(im)   
            img1.line(shape, fill =current_color, width = 0) 
        color2 = self.cl_team2
        color1 = (1,1,1)

        for i in range(8):
            current_color = (int(color1[0]+((color2[0]-color1[0])/8*i)),int(color1[1]+((color2[1]-color1[1])/8*i)),int(color1[2]+((color2[2]-color1[2])/8*i)))
            shape = [(0, i+8), (15, i+8)] 
            img1 = ImageDraw.Draw(im)   
            img1.line(shape, fill =current_color, width = 0) 
        font = ImageFont.truetype(os.path.join(os.path.dirname(__file__),"../src/pixelmix.ttf"), size=8)
        font2 = ImageFont.truetype(os.path.join(os.path.dirname(__file__),"../src/pixelated.ttf"), size=8)
        imDraw = ImageDraw.Draw(im)
        if score1!=0:
            imDraw.text((5,-1), str(score1), (192, 22, 222),font=font)
            imDraw.text((1,-2), "+", (192, 22, 222),font=font2)
        else:
            imDraw.text((1,-1), str(self.sc_team1), (230, 230, 230),font=font)
        if score2!=0:
            imDraw.text((5,8), str(score2), (0, 230, 0),font=font)
            imDraw.text((1,7), "+", (0, 230, 0),font=font2)
        else:
            imDraw.text((1,8), str(self.sc_team2), (230, 230, 230),font=font)
        if score1 == 0 and score2 ==0:
            im.save(os.path.join(os.path.dirname(__file__),"./manille.png"))  
        else:
            im.save(os.path.join(os.path.dirname(__file__),"./manilleUpd.png"))  
    def waitUpdate(self):
        print("updated")
        delta_score = input('Indicate score :')
        team = input('Indicate team (1 or 2) :')
        if int(team)==1:
            self.sc_team1 = self.sc_team1 + int(delta_score)
            self.generateImage(delta_score,0)
        else:
            self.sc_team2 = self.sc_team2 + int(delta_score)
            self.generateImage(0,delta_score)
        self.generateImage()
        return(self.getImage())

    def getImage(self, param=0):
        if param == 1:
            return(os.path.join(os.path.dirname(__file__),"./manilleUpd.png"))
        else:
            return(os.path.join(os.path.dirname(__file__),"./manille.png"))
