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
errmsg = re.findall(r'errmsg":"(.*?)"', res.text)[0]
print(errmsg)
