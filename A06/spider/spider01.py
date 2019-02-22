'''
简单的搜索引擎
    1) 数据来源,爬虫
        起点
        url :http://site.baidu.com/

    2) 起点页面 url
        页面的内容
        页面中的超链接
    3) 抓取超链接的各个页面 url
        页面的内容
        页面中的超链接



'''
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

# 抓取起点
# url = 'http://site.baidu.com/'
urls = ['http://site.baidu.com/']
old_urls = []

# 伪装浏览器的头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

def spider_url(url):
    # 保存该URL到已经抓取队列
    old_urls.append(url)

    # 构造请求对象, 伪装头信息
    req = Request(url, headers=headers)

    # 打开 请求对象
    response = urlopen(req)

    soup = BeautifulSoup(response.read(), 'html.parser')

    # 处理页面内容
    # 1) 页面的标题
    m_title = soup.title
    if m_title:
        title = m_title.get_text()
        print(title)

    # 2) 页面中的关键字
    m_keywords = soup.find('meta', attrs={'name': 'keywords'})
    if m_keywords:
        keywords = m_keywords.attrs.get('content')
        print(keywords)

    # 3) 抓取页面中的h1_h6 标签
    m_h1s = soup.find_all('h1')

    # 4) 抓取页面中所有的p标签
    m_ps = soup.find_all('p')

    context = ''
    for h1 in m_h1s:
        context += h1.get_text()

    for p in m_ps:
        context += p.get_text()

    print(context)

    # 获取页面中所有的超链接
    ls_a = soup.find_all('a')

    # 抓取超链接列表中的每一个页面
    for a in ls_a:
        a_url = a.attrs.get('href')

        # a_url不一定是一个有效的超链接
        if a_url == None:
            print('无效的连接')
            continue

        # 过滤非常规超链接
        res = re.match('^http[s]{0,1}://', a_url)

        if res == None:
            print('非正常链接')
            continue

        print(a_url)
        append_url(a_url)

def append_url(a_url):

    # 加入到队列中时,判断队列中是否已经有url
    if a_url in urls:
        print('队列中已经存在该URL')
        return

    # url已经抓取过
    if a_url in old_urls:
        print('已经抓取过该URL')
        return

    # 将URL加入到抓取队列
    urls.append(a_url)

if __name__ == '__main__':

    while True:
        # 从队列中, 取出一个连接, 抓取该链接的页面
        url = urls.pop(0)
        spider_url(url)

        # 将抓取到的数据保存到数据库中