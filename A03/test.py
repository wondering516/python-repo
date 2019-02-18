'''
# Filename : test.py
# author by : www.runoob.com

# 写文件
with open("test.txt", "wt") as out_file:
    out_file.write("该文本会写入到文件中\n看到我了吧！")

# Read a file
with open("test.txt", "rt") as in_file:
    text = in_file.read()

print(text)




from urllib import request,parse
import random

url="https://search.bilibili.com/all?"

keyword={"keyword":"翟天临","from_source":"banner_search","page":5}

keyword=parse.urlencode(keyword)

terminal=url + keyword

req = request.Request(terminal)

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
    with open("success.html","w+",encoding="utf-8") as fp:
        fp.write(result)



from urllib import request,parse
import random

# 定义函数 - 爬取网页
def load_data(search_data,n):
    # 菜鸟教程 - 搜索
    # 一定要考虑分页的参数是什么以及搜索的关键字是什么
    url = "http://search.jumei.com/?from=&cat=&"

    # 拼接请求的参数[查询条件,分页]
    # http://www.runoob.com/?s=js&page=2
    query_string = {"search": search_data, "filter": "0-11-{0}".format(n)}

    # 拼接url和query_string
    # 将query_string[字典类型dict]转换成url参数的key=value的形式
    query_string = parse.urlencode(query_string)
    # print(query_string)
    url = url + query_string

    print(url)

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
        with open("苹果聚美{0}.html".format(n), "w+", encoding="utf-8") as fp:
            fp.write(result)

# 调用函数
for n in range(1,3):
    load_data('苹果',n)





# 导入requests模块
import requests
import random

url = "https://www.liepin.com/zhaopin/?init=-1&headckid=58f2b888e920cc82&fromSearchBtn=2&sfrom=click-pc_homepage-centre_searchbox-search_new&ckid=58f2b888e920cc82&degradeFlag=0&siTag=I-7rQ0e90mv8a37po7dV3Q%7EfA9rXquZc5IkJpXC-Ycixw&d_sfrom=search_fp&d_ckId=a1fa782c5e199d37bd007d8ce1419b85&d_curPage=0&d_pageSize=40&d_headId=a1fa782c5e199d37bd007d8ce1419b85&"

# 查询字符串
query_string = {
    "key":"Java",
    "curPage":2
}

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

headers = {"User_Agent":user_agent}

# 发送请求
with requests.get(url = url,params=query_string,headers = headers) as resp:
    data = resp.text
    with open("liepin.html","w+",encoding="utf-8") as f:
        f.write(data)




import lxml.html

# 获取etree
etree = lxml.html.etree
print(etree) # <module 'lxml.etree' from 'E:\\python\\test_python\\venv\\lib\\site-packages\\lxml\\etree.cp36-win32.pyd'>

# 获取html解析器 - 确定解析的编码
html_parse = etree.HTMLParser(encoding="utf-8")
# 加载html页面
html = etree.parse("liepin.html",html_parse)
# print(html) # <lxml.etree._ElementTree object at 0x027EC030>

titles = html.xpath("//div[@class='job-info']/h3/a")

salary = html.xpath("//p[@class='condition clearfix']/span[1]")

for t in titles:
    # 获取标签中的内容,去除左右空格
    print(t.text.strip())

for s in salary:
    print(s.text)




import requests
from bs4 import BeautifulSoup


def download_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url, headers=headers)
    return r.text


def get_content(html, page):
    output = """第{}页 作者：{} 性别：{} 年龄：{} 点赞：{} 评论：{}\n{}\n------------\n"""
    soup = BeautifulSoup(html, 'html.parser')
    con = soup.find(id='content-left')
    con_list = con.find_all('div', class_="article")
    for i in con_list:
        author = i.find('h2').string  # 获取作者名字
        content = i.find('div', class_='content').find('span').get_text()  # 获取内容
        stats = i.find('div', class_='stats')
        vote = stats.find('span', class_='stats-vote').find('i', class_='number').string
        comment = stats.find('span', class_='stats-comments').find('i', class_='number').string
        author_info = i.find('div', class_='articleGender')  # 获取作者 年龄，性别
        if author_info is not None:  # 非匿名用户
            class_list = author_info['class']
            if "womenIcon" in class_list:
                gender = '女'
            elif "manIcon" in class_list:
                gender = '男'
            else:
                gender = ''
            age = author_info.string   # 获取年龄
        else:  # 匿名用户
            gender = ''
            age = ''

        save_txt(output.format(page, author, gender, age, vote, comment, content))


def save_txt(*args):
    for i in args:
        with open('qiubai.txt', 'a', encoding='utf-8') as f:
            f.write(i)


def main():
    # 我们点击下面链接，在页面下方可以看到共有13页，可以构造如下 url，
    # 当然我们最好是用 Beautiful Soup找到页面底部有多少页。
    for i in range(1, 14):
        url = 'https://qiushibaike.com/text/page/{}'.format(i)
        html = download_page(url)
        get_content(html, i)

if __name__ == '__main__':
    main()










import lxml.html

# 获取etree
etree = lxml.html.etree
print(etree) # <module 'lxml.etree' from 'E:\\python\\test_python\\venv\\lib\\site-packages\\lxml\\etree.cp36-win32.pyd'>

# 获取html解析器 - 确定解析的编码
html_parse = etree.HTMLParser(encoding="utf-8")
# 加载html页面
html = etree.parse("liepin.html",html_parse)
# print(html) # <lxml.etree._ElementTree object at 0x027EC030>

titles = html.xpath("//div[@class='job-info']/h3/a")

salary = html.xpath("//p[@class='condition clearfix']/span[1]")

for t in titles:
    # 获取标签中的内容,去除左右空格
    print(t.text.strip())

for s in salary:
    print(s.text)
'''


from urllib import request,parse
import random

#http://tieba.baidu.com/f?ie=utf-8&kw=java&pn=150

url = "http://tieba.baidu.com/f?ie=utf-8&"

keyword = input("请输入你想要搜索的关键字 : ")

page = int(input("请输入你想首先跳转的页数 : "))

end = int(input("你想查看几页的数据 : "))

keyword = {"kw": keyword, "pn": page}

keyword = parse.urlencode(keyword)

url = url + keyword

def search_data(keyword,page):
    keyword = {"kw": keyword, "pn": (page-1)*50}

    keyword = parse.urlencode(keyword)

    url = "http://tieba.baidu.com/f?ie=utf-8&"

    url = url + keyword

    print(url)
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
        with open("百度贴吧.html", "w+", encoding="utf-8") as fp:
            fp.write(result)
            print(result)

if __name__ == '__main__':

    for p in range(page,page+end+1):

        search_data(keyword,p)












































