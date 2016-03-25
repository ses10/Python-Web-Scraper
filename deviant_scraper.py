'''
deviant_scraper.py

Scrapes the images from a DeviantArt search page.

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
