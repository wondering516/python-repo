from spider05 import get_one_page
from spider03 import save, find_by_title
from bs4 import BeautifulSoup
import re

def get_movie_info(html):
    soup = BeautifulSoup(html, 'html.parser')

    ls_dd = soup.select('.board-wrapper dd')

    # 定义一个空列表, 存放电影的数据
    ls = []

    for dd in ls_dd:

        movie = {}

        a = dd.find('a', attrs={"class": 'image-link'})
        title = a.get('title')
        # print(title)
        movie['title'] = title

        p = dd.find('p', attrs={'class': 'star'})
        star = p.get_text()

        # print(star)

        # 正则表达式
        '''
            定义一个规则
        '''
        # print(type(star))
        star = star.replace('\n', '')
        # print(star)
        regx = '^.*?：(.*?)\s'
        res = re.match(regx, star)
        # print(res.group(1))
        movie['star'] = res.group(1)

        p = dd.find('p', attrs={'class': 'releasetime'})
        release_time = p.get_text()
        regx = '^.*?：([0-9-]+).*'
        res = re.match(regx, release_time)
        # print(res.group(1))
        movie['time'] = res.group(1)

        regx = '^.*?\((.*)\)'
        res = re.match(regx, release_time)
        if res :
            # print(res.group(1))
            movie['country'] = res.group(1)

        p = dd.find('p', attrs={'class': 'score'})
        i_int = p.find('i', attrs={'class': 'integer'})
        i_fra = p.find('i', attrs={'class': 'fraction'})

        score = i_int.get_text() + i_fra.get_text()

        # i = 10
        # s = str(i)
        # i = int(s)
        # print(float(score))
        movie['score'] = float(score)

        ls.append(movie)

    return ls

if __name__ == '__main__':

    movie_list = []

    for index in range(0, 10):
        html = get_one_page(index)
        movie_list += get_movie_info(html)

    # 使用数据库保存数据
    print((movie_list))

    # SQLite
    for movie in movie_list:
        save(movie)

    #  查询操作
    #   用户输入一个key, 根据key查询所有标题中包含key 的电影
    key = input('请输入您要查询的电影关键字： ')

    # 调用find
    ls = find_by_title(key)

    # 打印
    for movie in ls:
        print(movie)


'''
作业
    1. 解析贴吧列表
    2. 保存到数据库中

'''


