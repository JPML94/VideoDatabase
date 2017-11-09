from openpyxl import Workbook, load_workbook
import urllib.request
import time

wb = load_workbook('VIMEO.xlsx') #name of spreadsheet
ws = wb.active
sheet_ranges = wb['Form Responses 1'] #name of sheet

#print(sheet_ranges['AQ'])
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

for row in sheet_ranges['C']:
    title = row.value
    titles.append(title)
    #print(titles)
i = 0

for link in links:
    try:
        url = "ytimg/%s.jpg" % titles[i]
        if url.find("wistia") is  -1:
            if url.find("vimeo") is  -1:
                if url.find("facebook") is  -1:
                    if url.find("Link") is  -1:
                        if url.find("eventbrite") is  -1:
                            if url.find("feature") is  -1:
                                if url.find("=") is  -1:
                                    #urllib.request.urlretrieve(link, "ytimg/%s.jpg" % (title))
                                    #urllib.request.urlretrieve(link,url)
                                    #time.sleep(1)
                                    fname = url
                                    with urllib.request.urlopen(link) as d, open(fname, "wb") as opfile:
                                        print("works")
                                        data = d.read()
                                        opfile.write(data)

                                    i +=1

    except (RuntimeError, TypeError, NameError, urllib.error.HTTPError, FileNotFoundError):
        pass
print (len(links))
print(len(titles))

#for title in titles:
    #imgs = urllib.request.urlretrieve(links, "ytimg/img.jpg")


#urllib.request.urlretrieve("https://img.youtube.com/vi/lt4CYzsAWds/0.jpg", "ytimg/local-filename.jpg")
#wb.save('test.xlsx')
#print(links)
#print(titles)
        #if !(url.find("wistia") or url.find("vimeo") or url.find("facebook") or url.find("Link") or url.find("eventbrite") or url.find("feature")  or url.find("=")):
