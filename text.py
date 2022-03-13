import json
import re

import requests

productId = "7c1208da-907a-4391-9901-35a60096a3f9/b0ae0105-c979-4006-8582-1acf84b48fe0"
url = "https://j1.pupuapi.com/client/product/storeproduct/detail/" + productId

head = {
    # headerUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
res = requests.get(url, headers=head)
jsonshopping=json.loads(res.text)
price = jsonshopping['data']['price']
print(jsonshopping)
print(price)

url = "https://j1.pupuapi.com/client/product/storeproduct/detail/" + productId

head = {
            # headerUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
        }

res = requests.get(url, headers=head)



jsonshopping = json.loads(res.text)
try:
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

except:
    errmsg = re.findall(r'errmsg":"(.*?)"', res.text)[0]
    print(errmsg)