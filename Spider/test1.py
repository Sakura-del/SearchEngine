# -*-coding:utf-8-*-
import requests, pprint
import json
if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
    data = {
        'op': 'keyword',
        'cname': '',
        'pid': '',
        'keyword': '北京',
        'pageIndex': '1',
        'pageSize': '10'
    }
    headers = {
        'Cookie': 'route - cell = ksa;Hm_lvt_1039f1218e57655b6677f30913227148 = 1625320174;Hm_lpvt_1039f1218e57655b6677f30913227148 = 1625320174;SERVERID = 02f4c994014ba2083ffa81762e56b1a0 | 1625321488 | 1625320172',
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 91.0.4472.124Safari / 537.36Edg / 91.0.864.64'
    }
    response = requests.post(url=url,headers = headers,data = data)
    pprint.pprint(response.json())

