from urllib.request import urlopen
from urllib.parse import quote, urlencode



key = input('请输入一个查询关键字')

print(quote(key))

args = {
    'wd' : key,
    'ie' : 'utf-8'
} #  =>  wd= %%%%%%&ie=utf-8

print(urlencode(args))

url = 'http://www.baidu.com/s?'+ urlencode(args)

response = urlopen(url)  # get请求



print(response.read().decode())

