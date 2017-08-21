# -*- coding: utf-8 -*-
__author__ = 'duohappy'
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'}


def get_yiguo_price(url):
    web_source = requests.get(url, headers=headers)
    web_source.encoding = 'utf-8'

    web_data = web_source.text
    soup = BeautifulSoup(web_data, 'lxml')
    title_tag = soup.select('div.product-info div.summary-name h1')[0]
    price_tag = soup.select('div.pro-price div span strong')[0]
    return (title_tag.text, price_tag.text)  # 返回一个元组


if __name__ == '__main__':
    url = 'http://www.yiguo.com/product/1294029.html'
    get_yiguo_price(url)