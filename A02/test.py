import pickle
import os

datafile = 'xxx.data'
line = '======================================='
message = '''
=======================================
Welcome bookmark:
    press 1 to show list
    press 2 to add book
    press 3 to edit book
    press 4 to delete book
    press 5 to search book
    press 6 to show menu
    press 0 to quit
=======================================
'''
print(message)

class Person(object):
    """图书"""
    def __init__(self, name, Author):
        self.name = name
        self.Author = Author

# 获取数据
def get_data(filename=datafile):
    # 文件存在且不为空
    if os.path.exists(filename) and os.path.getsize(filename):
        with open(filename,'rb') as f:
            return pickle.load(f)
    return None

# 写入数据
def set_data(name, Author, filename=datafile):

    personList = {} if get_data() == None else get_data()

    with open(filename,'wb') as f:
        personList[name] = Person(name,Author)
        pickle.dump(personList,f)

# 保存字典格式的数据到文件
def save_data(dictPerson, filename=datafile):
    with open(filename,'wb') as f:
        pickle.dump(dictPerson,f)

# 显示所有图书
def show_all():
    personList = get_data()
    if personList:
        for v in personList.values():
            print(v.name,v.Author)
        print(line)
    else:
        print('not yet book,please add book')
        print(line)

# 添加图书
def add_person(name,Author):
    set_data(name,Author)
    print('success add book')
    print(line)

# 编辑图书
def edit_person(name,Author):
    personList = get_data()
    if personList:
        personList[name] = Person(name,Author)
        save_data(personList)
        print('success edit book')
        print(line)

# 删除图书
def delete_person(name):
    personList = get_data()
    if personList:
        if name in personList:
            del personList[name]
            save_data(personList)
            print('success delete book')
        else:
            print(name,' is not exists in dict')
        print(line)


# 搜索图书
def search_person(name):
    personList = get_data()
    if personList:
        if name in personList.keys():
            print(personList.get(name).name, personList.get(name).Author)
        else:
            print('No this book of ',name)
        print(line)


while True:
    num = input('>>')

    if num == '1':
        print('show all bookList:')
        show_all()
    elif num == '2':
        print('add books:')
        name = input('input bookname>>')
        Author = input('input Author>>')
        add_person(name, Author)
    elif num == '3':
        print('edit book:')
        name = input('input bookname>>')
        Author = input('input Author>>')
        edit_person(name, Author)
    elif num == '4':
        print('delete book:')
        name = input('input bookname>>')
        delete_person(name)
    elif num == '5':
        print('search :')
        name = input('input bookname>>')
        search_person(name)
    elif num == '6':
        print(message)
    elif num == '0':
        break
    else:
        print('input error, please retry')