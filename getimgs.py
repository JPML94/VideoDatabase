from openpyxl import Workbook, load_workbook
import requests
import random
from PIL import Image
import os, sys



wb = load_workbook('VIMEO.xlsx') #name of spreadsheet
ws = wb.active
sheet_ranges = wb['Form Responses 1'] #name of sheet


links = []
titles = []

for row in sheet_ranges['B']: #column
    #sheet_ranges.append(row)
    x = row.value.replace("https://www.youtube.com/embed/", "")
    link = "https://img.youtube.com/vi/" + x + "/0.jpg"
    links.append(link)


    #x = row.value.split(',')[ 1:] https://www.youtube.com/embed/7WH8uxXXe9o
    #x = ','.join(x)
    #print (link)

arr = []
imgname = []

for row in sheet_ranges['C']:
    title = row.value
    titles.append(title)
#wdrv

s = requests.Session()
i = 0
for link in links:
    if link.find("wistia") is  -1:
        if link.find("vimeo") is  -1:
            if link.find("facebook") is  -1:
                if link.find("Link") is  -1:
                    if link.find("eventbrite") is  -1:
                        if link.find("digiday") is  -1:
                            if link.find("feature") is  -1:
                                if link.find("=") is  -1:
                                    if link.find("wdrv") is  -1:
                                        print(link + "\n")
                                        x = s.get(link)
                                        x.raise_for_status()
                                        url = titles[i]
                                        url = url.replace("/", " ")
                                        url = url.replace("|", " ")
                                        url = url.replace("*", " ")
                                        url = url.replace("?", " ")
                                        url = url.replace("…", " ")
                                        url = url.replace(",", " ")
                                        url = url.replace("\"", " ")
                                        url = url.replace("\t", " ")
                                        url = url.replace(":", " ")
                                        url = url + ".jpg"
                                        imgname.append(url)
                                        with open("ytimg/" + url, 'wb') as handle:
                                            for block in x.iter_content(1024):
                                                handle.write(block)
                                    else:
                                            arr.append(titles[i])
                                else:
                                        arr.append(titles[i])
                            else:
                                    arr.append(titles[i])
                        else:
                                arr.append(titles[i])
                    else:
                            arr.append(titles[i])
                else:
                        arr.append(titles[i])
            else:
                    arr.append(titles[i])
        else:
                arr.append(titles[i])
    else:
            arr.append(titles[i])
    i +=1

#print(len(arr))
#print(arr)
