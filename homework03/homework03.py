from urllib import request,parse
import random

#http://tieba.baidu.com/f?ie=utf-8&kw=java&pn=150
#http://tieba.baidu.com/f?kw=java&ie=utf-8&pn=150

keyword = input("请输入你想要搜索的关键字 : ")

page = int(input("请输入你想首先跳转的页数 : "))

end = int(input("你想查看几页的数据 : "))

def search_save_data(keyword,page):
    keyword=str(keyword)

    page=str((page-1)*50)

    keyword = {"kw": keyword, "ie":"utf-8","pn": page}

    keyword = parse.urlencode(keyword)

    url = "http://tieba.baidu.com/f?"

    url = url + keyword

    print(url)
    print("="*100)
    # 构建出完整的url
    req = request.Request(url)

    # 伪装公共的浏览器
    user_agents_list = [
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
    req.add_header("User_Agent", user_agent)

    # 发送请求
    # req参数既包含url,又包含user_agent
    with request.urlopen(req) as resp:
        data = resp.read()
        result = data.decode()  # 转义成字符串

        # 写入到文件中
        with open("百度贴吧.{}.html".format(page), "w+", encoding="utf-8") as fp:
            fp.write(result)
            print(result)


if __name__ == '__main__':

    for p in range(page,page+end):

        search_save_data(keyword,p)


