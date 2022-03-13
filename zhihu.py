import json

import requests
import re


def request_url(userName):
    url = 'https://www.zhihu.com/people/' + userName + '/collections'
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'
    }
    res = requests.get(url, headers=head)
    #收藏夹的名字数组
    name = re.findall(r'"noreferrer noopener">(.*?)</a>', res.text)
    #收藏夹链接数组
    href = re.findall(r'href="/collection(.*?)"', res.text)
    for i in range(0, len(name)):
        print("收藏夹名："+name[i])
        url_collection = 'https://www.zhihu.com/collection'
        url_collection = url_collection + href[i]
        print(url_collection)


if __name__ == '__main__':
    userName = "shuai-qi-66-47"
    request_url(userName)
