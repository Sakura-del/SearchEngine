# -*-coding:utf-8-*-
from lxml import etree
import requests, json
import re
from multiprocessing import Pool
import random
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'

}
url = 'https://www.pearvideo.com/category_5'
page_text = requests.get(url=url, headers=headers).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@class ="listvideo-list clearfix"]/li')
urls = []

for li in li_list:
    detail_url = 'https://www.pearvideo.com/'+li.xpath("./div/a/@href")[0]
    name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'

    countId = detail_url.split("/")[-1].split("_")[1]
    print(countId)
    random.seed(time.time())

    ajax_url = 'https://www.pearvideo.com/videoStatus.jsp'
    params = {
        'countId' : countId,
        'mrd': str(random.random())
    }
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56',
        'Referer': detail_url,
        'Cookie': '__secdyid=d3ce09f128a170b04671831f89be880c7598c46e292cdb51021625458058; JSESSIONID=BF13D0C862B2536F029A475BBD138DAC; PEAR_UUID=bf8cb835-7dd0-4135-b066-d03d3921368c; _uab_collina=162545805851571985754291; UM_distinctid=17a74d9a6778f1-06aedee5b66a-7a697e6d-144000-17a74d9a678bd0; CNZZDATA1260553744=1353905273-1625456870-https%253A%252F%252Fwww.baidu.com%252F%7C1625456870; Hm_lvt_9707bc8d5f6bba210e7218b8496f076a=1625458059; p_h5_u=4465A128-7337-4DAE-9998-989CD525F7F7; acw_tc=76b20f4816254608223574491e11a55b193b052797b5d63cc2d38f1ada5a79; Hm_lpvt_9707bc8d5f6bba210e7218b8496f076a=1625461156; SERVERID=bacac21aafa9027952fdc46518c0c74f|1625461232|1625458058'
      }
    video_json = requests.get(url = ajax_url,headers = header,params=params).json()
    print(video_json)

    fake_url = video_json['videoInfo']['videos']['srcUrl']
    # 对假地址进行处理，并把刚才的countId组合起来
    fake_url_list = fake_url.split('/')
    end = fake_url_list.pop()  # 删除不必要的字符串
    end_list = end.split("-")
    end_url = ""  # end_url是一个结尾字符串
    for i in range(len(end_list) - 1):
        end_url = end_url + "-" + end_list[i + 1]

    # 真实的地址，先用假地址，然后组合countId
    rea_url = ""
    for element in fake_url_list:
        rea_url = rea_url + element + "/"
    rea_url = rea_url + "cont-" + str(countId) + end_url

    dic = {
        'url':rea_url,
        'name':name
      }
    urls.append(dic)


def get_video(dic):
    url = dic['url']
    data = requests.get(url=url, headers=headers).content

    with open(dic['name'],'wb') as fp:
        fp.write(data)
        print(dic['name'],'下载成功')


pool = Pool(4)
pool.map(get_video, urls)

pool.close()
pool.join()


