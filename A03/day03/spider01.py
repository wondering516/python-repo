'''
External Libraries
    Python 3.6
        Lib 文件夹
            urllib  Python 内置库
'''
# 引入 urllib库
# import urllib.request
# from urllib import request
from urllib.request import urlopen

# 通过URL 获取他的HTML代码
url = 'https://www.csdn.net/'
# 打开指定的URL，　获取返回的内容
response = urlopen(url)

# 打印获取到的HTML 二进制表示形式
# print(response.read())

# 字符转换
print(response.read().decode('utf-8'))

# request的其它信息
print(response.geturl())

# request的头信息
print(response.info())

print(response.getheaders())

print(response.getheader('Server'))
