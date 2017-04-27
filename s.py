from lxml import html
import csv, os, json
import requests
from exceptions import ValueError
from time import sleep
url="http://www.shopclues.com/lg-nexus-5-16gb-18.html"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
page = requests.get(url, headers=headers)
doc = html.fromstring(page.content)
XPATH_NAME = '//h1[@itempop="name"]//text()'
XPATH_PRODUCTID = '//span[@class="pID"]//text()'
XPATH_DISCOUNTED_PRICE = '//span[@class="f_price"]//text()'
XPATH_SALE_PRICE = '//span[@id="sec_discounted_price_"]//text()'
XPATH_ORIGINAL_PRICE = '//span[@class="sec_list_price_"]//text()'
XPATH_DISCOUNT = '//span[@class="discount"]//text()'
XPATH_OFFER = '//div[@class="offers"]//text()'

RAW_NAME = doc.xpath(XPATH_NAME)
RAW_PRODUCTID = doc.xpath(XPATH_PRODUCTID)
RAW_DISCOUNTED_PRICE = doc.xpath(XPATH_DISCOUNTED_PRICE)
RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)
RAW_ORIGINAL_PRICE = doc.xpath(XPATH_ORIGINAL_PRICE)
RAW_DISCOUNT = doc.xpath(XPATH_DISCOUNT)
RAW_OFFER = doc.xpath(XPATH_OFFER)

NAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
PRODUCTID = ' '.join(''.join(RAW_PRODUCTID).split()).strip() if RAW_PRODUCTID else None
DISCOUNTED_PRICE = ' '.join(''.join(RAW_DISCOUNTED_PRICE).split()).strip() if RAW_DISCOUNTED_PRICE else None
SALE_PRICE = ' '.join(''.join(RAW_SALE_PRICE).split()).strip() if RAW_SALE_PRICE else None
ORIGINAL_PRICE = ''.join(RAW_ORIGINAL_PRICE).strip() if RAW_ORIGINAL_PRICE else None
DISCOUNT = ''.join(RAW_DISCOUNT).strip() if RAW_DISCOUNT else None
OFFER = ''.join(RAW_OFFER).strip() if RAW_OFFER else None

data = {
            'NAME': NAME,
            'PRODUCTID': PRODUCTID,
            'DISCOUNTED_PRICE': DISCOUNTED_PRICE,
            'SALE_PRICE': SALE_PRICE,
            'ORIGINAL_PRICE': ORIGINAL_PRICE,
            'ORIGINAL_PRICE': ORIGINAL_PRICE,
            'DISCOUNT': DISCOUNT,
            'OFFER': OFFER,
            'URL': url,
        }

extracted_data = []
extracted_data.append(data)
sleep(5)
f=open('mamamama.json','w')
json.dump(extracted_data,f,indent=4)
