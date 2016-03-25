'''
deviant_scraper.py

Scrapes the images from a DeviantArt search page.

So far only scrapes from 1st results page
'''
from lxml import html
import requests

#what image to search for, spaces have to be replaced by "+" in query
query = 'adventure+time'
queryString = 'http://www.deviantart.com/browse/all/?section=&global=1&q=' + query
#the current xPath for image results as of writing
xPath = '//*[@id="page-1-results"]/div/span/span[1]/span[2]/a/img'

#get page and parse it
page = requests.get(queryString)
tree = html.fromstring(page.content)

#get the images
images = tree.xpath(xPath)

#output images to html file
f = open("deviantart-results.html", 'w')

f.write('''
    <!Doctype HTML5>
    <html>
        <body>
            <ul>
''')


#write each image url
for image in images:
    f.write('<li><img src="' + image.get('src') + '" ></li>' )

f.write('''
            </ul>
        </body>
    </html>
''')

f.close()
