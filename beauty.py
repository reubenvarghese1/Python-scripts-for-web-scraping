import urllib
import lxml.html
connection = urllib.urlopen('http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=iphone')

dom =  lxml.html.fromstring(connection.read())

for link in dom.xpath('//li[@id="result_0"]/@data-asin'): # select the url in href for all a tags(links)
    print link
