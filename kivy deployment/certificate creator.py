from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import numpy as np
from kivymd.app import MDApp
from kivy.lang.builder import Builder

KV='''
MDBoxLayout:
    orientation:"vertical"
    MDToolbar:
        title : "certificate creator"
    MDBoxLayout:
        orientation : "vertical"
        MDLabel:
            text :"codeaj"

'''


class PosterCreator(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    PosterCreator().run()

'''class Data():
    def __init__(self,name,date,course,collage,outimg):
        self.name=name
        self.date=date
        self.course=course
        self.collage=collage
        self.outimg=outimg

    def imgCreate(self,templates,logo,fontsize,text,color_R,color_G,color_B,font,pos_x,pos_y):
        img = Image.open(templates)
        img2=Image.open(logo)
        draw = ImageDraw.Draw(img)
        img.paste(img2, (300, 50))
        font = ImageFont.truetype(font, fontsize)
        draw.text((pos_x,pos_y),text, fill=(color_R,color_G,color_B), font=font)
        img.save(f"{self.outimg}")


    def AddText(self,fontsize,text,color_R,color_G,color_B,font,pos_x,pos_y):
        img = Image.open(self.outimg)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font, fontsize)
        draw.text((pos_x,pos_y),text, fill=(color_R,color_G,color_B), font=font)
        img.save(f"{self.outimg}")


    def AddImage(self,logo,logopos_x,logopos_y):
        img = Image.open(self.outimg)
        img2 = Image.open(logo)
        img.paste(img2, (logopos_x, logopos_y))
        img.save(f"{self.outimg}")



all_data=[]
for j in range (0,4):
    ex=pd.read_excel('codeaj.xlsx', index_col=0,usecols=[j])
    for i in range(0,len(ex)):
        all_data.append(ex.index[i])

split=np.array_split(all_data,4)

for i in range(0,len(ex)):
    #print(split[0][i] , split[1][i], split[2][i],split[3][i])
    obj=Data(split[0][i].upper(),f'{split[1][i]}',f'{split[2][i]}',f"{split[3][i]}",f'{split[0][i]}.png')
    t=f"is hereby awardes this certificate of achievement for the successful \n           completion of The {obj.course} course certification exam \n                                            on {obj.date} "
    obj.imgCreate('bg.jpg','logo.png',50,obj.name,150,59,88,'namefont.ttf',320,200)
    obj.AddText(20,t,1,1,1,'textfont.ttf',150,280)
    obj.AddText(15,'Ajay,ceo of codeAj',150,132,139,'namefont.ttf',80,500)
    obj.AddText(15,'Neeraj Sharma, HOD of CS',1,1,1,'namefont.ttf',650,500)
    obj.AddImage('codeajlogo.jpg',280,450)
    obj.AddImage('cistlogo.jpg',480,450)
    print(f"{split[0][i]}.png created !!")

'''
'''img=cv2.imread(obj.outimg)
cv2.imshow('o/p banner' , img)
cv2.waitKey(0)'''



