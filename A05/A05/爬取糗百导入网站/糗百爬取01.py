'''
抓取猫眼网Top100榜
'''

from urllib.request import urlopen

'''     https://maoyan.com/board/4?offset=10
        https://maoyan.com/board/4?offset=20

        ...
        https://maoyan.com/board/4?offset=90

'''


def get_one_page(index):  # 从0 到 9结束
    url = "http://xiaohua.zol.com.cn/new/{}.html".format(index)

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


def save_one_page(index, html):
    # 数据保存到文件中
    # 文件名    maoyan_top100_page_index.html
    # 文件存到什么地方
    #file_name = '糗百html\\

    # 打开一个文件
    '''
        r   以字符串的方式 只读
        w   以字符串的方式 只写
        a   以字符串的方式 追加

        rb
        wb
        ab

        r+  w+ a+

    '''
    # file = open(file_name, 'w', encoding='utf-8')
    #
    # file.write(html)
    #
    # file.close()

    with open("爆笑{}.html".format(index), 'w', encoding='utf-8') as file:
        file.write(html)


# __name__ 内置变量
# 当执行是当前文件(模块)时, __name__ = '__main__'
# 当当前文件是被其它文件引用 时, __name__ = 模块名

# get_one_page(9)

if __name__ == '__main__':

    for index in range(0, 10):
        # 获取单页数据
        html = get_one_page(index)

        # 保存单页数据
        save_one_page(index, html)

'''
作业:
    1. 百度贴吧 https://tieba.baidu.com/f ? .....
    2. 用户输入一个关键字, 
    3. 取出前5页, 保存到文件中
'''