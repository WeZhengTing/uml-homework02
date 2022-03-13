import json
from time import strftime, sleep

import requests
import re


def pupuMessage(productId):
    try:
        url = "https://j1.pupuapi.com/client/product/storeproduct/detail/" + productId
        head = {
            # headerUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
        }

        res = requests.get(url, headers=head)

        jsonshopping = json.loads(res.text)
        # res.encoding="utf-8"
        # 得到商品名字
        # name = re.findall(r'name":"(.*?)",', res.text)[0]
        name = jsonshopping['data']['name']
        # 得到商品规格
        # spec = re.findall(r'spec":"(.*?)",', res.text)[0]
        spec = jsonshopping['data']['spec']
        # 得到商品当前价格
        # price = re.findall(r'price":(.*?),', res.text)[0]
        price = jsonshopping['data']['price']
        price = str(int(price) / 100)

        # 得到商品市场价格
        # market_price = re.findall(r'market_price":(.*?),', res.text)[0]
        market_price = jsonshopping['data']['market_price']
        market_price = str(int(market_price) / 100)

        # 得到商品市场详细信息
        # share_content = re.findall(r'share_content":"(.*?)",', res.text)[0]
        share_content = jsonshopping['data']['share_content']

        print("--------------" + name + "----------")
        print("规格：" + spec)
        print("价格：" + price)
        print("原价/折扣价：" + market_price + "/" + price)
        print("详细内容：" + share_content)
        print("\n\n--------------" + name + "的价格波动----------")
    except:
        url = "https://j1.pupuapi.com/client/product/storeproduct/detail/" + productId

        head = {
            # headerUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
        }

        res = requests.get(url, headers=head)
        errmsg = re.findall(r'errmsg":"(.*?)"', res.text)[0]
        print(errmsg)


def now_price(productId):
    try:
        while (1):
            url = "https://j1.pupuapi.com/client/product/storeproduct/detail/" + productId

            head = {
                # headerUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
            }
            res = requests.get(url, headers=head)
            price = re.findall(r'price":(.*?),', res.text)[0]
            price = str(int(price) / 100)
            nowTimeAndPrint = strftime('%Y' + '-' + '%m' + '-' + '%d' + ' %H:%M,价格为' + price)
            print(nowTimeAndPrint)
            sleep(3)

    except:
        print("进程结束")


if __name__ == '__main__':
    productId = "7c1208da-907a-4391-9901-35a60096a3f9/44e7652b-a90e-4328-a89f-74471de7e218"
    pupuMessage(productId)
    now_price(productId)
