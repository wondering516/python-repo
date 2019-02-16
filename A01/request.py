'''
导入requset模块，通过链接打开网站，将网页源码显示在屏幕上并下载到"baidu.html"中，
'''

from urllib import request

url="http://www.baidu.com"

with request.urlopen(url) as resp:
    data = resp.read()
    result=data.decode()
    print(result)
    with open('baidu.html','w+',encoding='utf-8') as fp:#此方法不需要close()
        fp.write(result)
