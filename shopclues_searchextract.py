import urllib
import lxml.html
from bs4 import BeautifulSoup

connection = urllib.urlopen('http://www.shopclues.com/search?q=iphone 7')

dom = lxml.html.fromstring(connection.read())
# li = dom.find("div", {"class": "column col3"})
count = 0
for link in dom.xpath("//div[@class='column col3']/descendant::*[@href][1]/@href"):  # sgs(links)print link
    if count < 1:
        print link
        count = count + 1
    else:
        break
