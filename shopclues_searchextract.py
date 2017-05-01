import urllib
import lxml.html
from bs4 import BeautifulSoup
import requests
from lxml import html
import csv, os, json
import requests
from exceptions import ValueError
from time import sleep
import urllib
import lxml.html

urlprod = "http://www.shopclues.com/search?q=" + data + "&sc_z=2222&z=0"
headers = { 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0 '}
page = requests.get(urlprod, headers=headers)
dom = html.fromstring(page.content)
count = 0
for link in dom.xpath("//div[@class='column col3']/descendant::*[@href][1]/@href"):  # sgs(links)print link
    if count < 1:
        print link
        count = count + 1
    else:
        break
