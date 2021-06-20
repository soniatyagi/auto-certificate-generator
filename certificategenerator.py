from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
df = pd.read_csv('list.csv')
font = ImageFont.fontstyle.apply('arial',60)
for index,j in df.iterrows():
    img = Image.open('Certificate.jpg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(125,260),text='{}'.format(j['name']),fill=(0,0,0),font=font)
    img.save('pictures/{}.jpg'.format(j['name']))