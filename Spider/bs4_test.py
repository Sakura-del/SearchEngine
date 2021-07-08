# -*-coding:utf-8-*-

import json
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'Cookie': 'route - cell = ksa;Hm_lvt_1039f1218e57655b6677f30913227148 = 1625320174;Hm_lpvt_1039f1218e57655b6677f30913227148 = 1625320174;SERVERID = 02f4c994014ba2083ffa81762e56b1a0 | 1625321488 | 1625320172',
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 91.0.4472.124Safari / 537.36Edg / 91.0.864.64'
    }
    page = requests.get(url=url, headers=headers)
    page.encoding = 'gbk2312'
    soup = BeautifulSoup(page.text,'lxml')
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./sanguoyanyi.text','w',encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com/' + li.a['href']
        detail_text = requests.get(url=detail_url,headers=headers)
        detail_text.encoding = 'gbk2312'
        detail_soup = BeautifulSoup(detail_text.text,'lxml')
        detail_content = detail_soup.find('div', class_='chapter_content')
        # 文章内容
        content = detail_content.text.replace(u'\xa0', '')
        fp.write(title + ':'+content+'\n')
        print(title,'爬取完毕！！！')