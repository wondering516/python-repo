from bs4 import BeautifulSoup
import re
from urllib.request import urlopen


def get_one_page(index):  # 从0 到 9结束
    url = 'https://maoyan.com/board/4?offset={}'.format(index * 10)

    # url = 'https://maoyan.com/board/4?offset=%d'%(index*10)
    '''
    字符串的格式化处理
    {}  占位符
    使用format方式格式化字符串

    %

    '''
    print(url)

    response = urlopen(url)
    return response.read().decode()


for index in range(0, 10):
    html = get_one_page(index)

    soup = BeautifulSoup(html, 'html.parser')

    ls_dd = soup.select('.board-wrapper dd')

    for dd in ls_dd:
        a = dd.find('a', attrs={"class": 'image-link'})

        title = a.get('title')

        print(title)

        p = dd.find('p', attrs={'class': 'star'})

        star = p.get_text()

        print(star.strip())
    print("=" * 100)

'''

# 正则表达式

        #定义一个规则

    # print(type(star))
    star = star.replace('\n', '')
    # print(star)
    regx = '^.*?：(.*?)\s'
    res = re.match(regx, star)
    print(res.group(1))

'''
