from PIL import Image
import os, sys
from openpyxl import Workbook, load_workbook
from pathlib import Path

images = os.listdir("./")

#print(images)
i = 0
#my_file = Path('ytimg/{images[i]}')
#while my_file.exists():


for i in range(len(images)):
    if images[i].find("imgcrop") is  -1:
        img = Image.open(images[i])
        crop = (0, 45, 480, 315)
        img = img.crop(crop)
        img.save(images[i])
        i += 1
#img = Image.open('Apple - Perspective.jpg')
#crop = (0, 45, 480, 315)
#img = img.crop(crop)
#img.save('sompic.jpg')
