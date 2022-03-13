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
        href_head = 'https://www.zhihu.com/api/v4/collections'
        #构造子链接
        url_collection = href_head +href[i]+'/items?offset=0&limit=20'
        sonTitleAndUrlByHref(url_collection)

#通过子链接得到子文件的链接与标题
def sonTitleAndUrlByHref(href):
    try:
        head = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'
        }
        res = requests.get(href, headers=head)
        titlesAndUrl = re.findall(r'NORMAL",(.*?)","question', res.text)
        for i in range(0,len(titlesAndUrl)):
            url=re.findall(r'rl":"(.*?)","created_time',titlesAndUrl[i])
            title = re.findall(r'title":"(.*)', titlesAndUrl[i])
            print(title+url)
    except:
        return 0


if __name__ == '__main__':
    userName = "shuai-qi-66-47"
    request_url(userName)
