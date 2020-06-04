import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

regex = re.compile('[0-9]')
page_count = range(1, 6)


def get_search_result(search_product, product_brand):
    for count in page_count:
        url = requests.get('https://www.jumia.com.ng/phones-tablets/'+product_brand+'/?q='+search_product+'&page='+format(count))
        soup = BeautifulSoup(url.content, 'html.parser')
        result = soup.find(class_='-paxs row _no-g _4cl-3cm-shs')
        items = result.find_all('article')

        name_of_product = [item.find(class_='name').get_text() for item in items]
        price_of_product = [''.join(regex.findall(item.find(class_='prc').get_text())) for item in items]
        product_image = [item.find(class_='img').get('data-src') for item in items]
        product_link = [item.find('a').get('href') for item in items]

        # Save search result in a CVS file
        search_result = pd.DataFrame({
            'Name': name_of_product,
            'Product': price_of_product,
            'Image': product_image,
            'Product link': product_link
        }) 

        search_result.to_csv('search_result.csv', index=False, mode='a')

        print(search_result)


get_search_result('iphone+8', 'apple')


  
# Yessss Sir!!!!!!!!!!!!!!!!!!!!!!!! 