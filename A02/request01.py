'''
导入random模块与request模块
'''
from urllib import request
import random

#利用request模块构建出一个完整的URL包括浏览器的请求头信息（伪装成一个浏览器）

url = "http://www.taobao.com/"

#将url信息封装到request对象中
req = request.Request(url)

#伪装公共浏览器的请求头

user_agents_list=[
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
    ]
#随机获取一个代理
user_agent = random.choice(user_agents_list)

#在req添加user_agent
req.add_header("User_Agent",user_agent)

#发送请求
#req参数既包括又包含user_agent
with request.urlopen(req) as resp:
    data = resp.read()
    result = data.decode()#转移成字符串
    print(result)
    #写入文件
    with open("taobao_index.html","w+",encoding="utf-8") as fp:
        fp.write(result)


#成功将淘宝索引页面添加到文件中并打印到控制台