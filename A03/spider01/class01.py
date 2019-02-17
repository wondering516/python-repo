#两种导包方法
'''

#第一种
import urllib.request

url="http://www.taobao.com/"

response=urllib.request.urlopen(url)

print(response.read().decode("utf-8"))


#第二种
from urllib import request

url = "http://taobao.com/"

response = request.urlopen(url)

print(response.read().decode("utf-8"))
'''

from urllib.request import urlopen
from urllib.parse import quote

key = input("请输入你想要搜索的关键字 : ")

url = "http://www.baidu.com/wd="+quote(key)

response = urlopen(url)

print(response.read().decode("utf-8"))

