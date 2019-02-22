'''
抓取猫眼网Top100榜
'''

from urllib.request import urlopen



'''     https://maoyan.com/board/4?offset=10
        https://maoyan.com/board/4?offset=20

        ...
        https://maoyan.com/board/4?offset=90

'''




def get_one_page(index): # 从0 到 9结束
    url = 'https://maoyan.com/board/4?offset={}'.format(index*10)

    # url = 'https://maoyan.com/board/4?offset=%d'%(index*10)

    print(url)

    response = urlopen(url)

    return response.read().decode()

def save_one_page(index, html):
    # 数据保存到文件中
    # 文件名    maoyan_top100_page_index.html
    # 文件存到什么地方
    file_name = 'maoyan\\top100_page_{}.html'.format(index+1)

    # 打开一个文件
    # file = open(file_name, 'w', encoding='utf-8')
    #
    # file.write(html)
    #
    # file.close()

    with open(file_name, 'w', encoding='utf-8') as file:

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