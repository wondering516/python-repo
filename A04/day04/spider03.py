'''
SQLite
    MySQL
    SQL Server
    Oracle

    1) 关系型数据库
        关系表
            行 记录
            列 字段
    2) 基于文件的数据库
        只要有文件就可以直接使用

    3) SQL语言


在python 中使用SQLite

'''
import sqlite3
import os

db_file = 'maoyan.db'

# 创建表
def create_table():

    # 1. 连接数据库
    conn = sqlite3.connect(db_file)

    # 2. 创建执行对象
    cursor = conn.cursor()

    # 3. 执行SQL语句
    cursor.execute('''
        create table movie(
            id integer primary key autoincrement,
            title text,
            star text,
            reltime text,
            country text,
            score float
        )
    ''')

    # 4. 提交操作, 对于可以修改数据库内容的操作, 必须要提交
    conn.commit()

    # 5. 关闭连接
    conn.close()

def save(movie):
    # 1. 连接
    conn = sqlite3.connect(db_file)

    # 2. 创建执行对象
    cursor = conn.cursor()

    # 3. 执行SQL语句
    cursor.execute('''
        insert into movie 
        (title, star, reltime, country, score)
        values
        (?, ?, ?, ?, ?)
    ''', (movie.get('title'), movie.get('star'), movie.get('time'),
          movie.get('country'), movie.get('score')) )

    # 4. 提交
    conn.commit()

    # 5. 关闭
    conn.close()

# 根据标题关键字查询数据库
def find_by_title(key):

    # 1.
    conn = sqlite3.connect(db_file)

    # 2.
    cursor = conn.cursor()

    # 3.
    result = cursor.execute('''
        select * from movie
        where title like ?
    ''', ('%'+key+'%',))

    # 4. 查询不需要提交
    ls = []
    for row in result:
        movie = {}
        movie['id'] = row[0]
        movie['title'] = row[1]
        movie['star'] = row[2]
        movie['time'] = row[3]
        movie['country'] = row[4]
        movie['score'] = row[5]

        ls.append(movie)

    # 5. 关闭
    conn.close()

    return ls

if __name__ == '__main__':
    # 创建一个数据表
    if not os.path.exists(db_file):
        create_table()

    '''
    在项目下会出现一个maoyan.db文件
        1） PyCharm 右侧点击Database
        2） 点击 + 弹出菜单中， 选择Data Source， 再选择sqlite
        3)  如果有 Download missing driver files, 点击 Download
        4)  选择 file 选择需要打开的数据库文件 
        5） 能不能展开， maoyan.db
    '''

    # 保存
    movie = {'title': '霸王别姬', 'star': '张国荣,张丰毅,巩俐', 'time': '1993-01-01', 'score': 9.6}
    # save(movie)

    find_by_title('王')

