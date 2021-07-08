# -*-coding:utf-8-*-
from lxml import etree
import requests,json

if __name__ == '__main__':
    url = 'http://www.jobbole.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
    }
    page = requests.get(url,headers=headers)
    page.encoding = 'gbk2312'
    page_text = page.text
    tree = etree.HTML(page_text)
    a_list = tree.xpath('//div[@class = "list-item"]')
    all_city_names_list = []
    for a in a_list:
        url = a.xpath("./div[2]/div[1]/a/@href")[0]
        title = a.xpath('./div[2]/div[1]/a/h1/text()')[0]
        description = a.xpath('./div[2]/div[2]/text()')[0].split()[0]
        date = a.xpath('./div[2]/div[3]/div[1]/span/text()')[0]
        category = a.xpath('.//div[@class="title-tag "]/a/text()')[0]
        href = a.xpath('.//div[@class="content-title"]/a/@href')[0]
        print(href)
        print(category)
        # city_name = a.xpath('./text()')[0]
        # all_city_names_list.append(city_name)
        # print(city_name)


