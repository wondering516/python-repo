
from urllib import request,parse
import random

# 一定要考虑分页的参数是什么以及搜索的关键字是什么
url = "https://search.bilibili.com/all?"

# 拼接请求的参数[查询条件,分页]

query_string = {"keyword":"翟天临","from_source":"banner_search","page":4}

# 拼接url和query_string
# 将query_string[字典类型dict]转换成url参数的key=value的形式
query_string = parse.urlencode(query_string)
# print(query_string)
url = url + query_string
print(url)
# 构建出完整的url
req = request.Request(url)

# 伪装公共的浏览器
user_agents_list= [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
    ]

# 随机获取
user_agent = random.choice(user_agents_list)

# 在req添加user_agent
req.add_header("User_Agent",user_agent)

# 发送请求
# req参数既包含url,又包含user_agent
with request.urlopen(req) as resp:
    data = resp.read()
    result = data.decode() # 转义成字符串

    # 写入到文件中
    with open("bilibili.html","w+",encoding="utf-8") as fp:
        fp.write(result)
        #print(result)