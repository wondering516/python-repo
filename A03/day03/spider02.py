
from urllib.request import urlopen, Request

url = 'http://httpbin.org/get'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

# 创建请求对象
request = Request(url, headers=headers)

response = urlopen(request)

print(response.read().decode())


