import urllib2
from bs4 import BeautifulSoup

def parse_webpage(url):
    page = urllib2.urlopen(url)
    return page
    