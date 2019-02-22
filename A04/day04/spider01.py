from spider05 import get_one_page


html = get_one_page(0)

'''
解析HTML中的内容
    1) 使用BeautifulSoup库
    a. 安装BeautifulSoup4库
        在命令行中进入Python环境
        执行 pip install beautifulsoup4
        进入Python的交互模式 执行python命令
        import bs4  如果没有任何错误, 表明安装成功
        
        卸载 pip uninstall beautifulsoup4
            过程中需要输入 y
          
    b. 引入bs4  
    2) 使用XPath
    3) 使用pyquery
    
'''
from bs4 import BeautifulSoup

'''
由html代码, 生成BeautifulSoup的对象

BeautifulSoup在解析HTML时, 可以设置解析器
    1) html.parser
    2) lxml 
    3) 解析HTML5
'''
soup = BeautifulSoup(html, 'html.parser')

# 打印soup对象的内容
# print(soup.prettify())

# 获取 title标签  使用标签名获取标签节点
# 只能获取页面中第一个标签
title = soup.title

print(title.get_text())

print(soup.p)

'''
使用方法
find_all() 返回所有符合条件的标签对象
find()      只返回第一个符合条件的标签对象
'''
ls_p = soup.find_all('p')

for p in ls_p:
    print(p)

p = soup.find('p')


body = soup.body

# 打印出标签的所有的HTML代码
print(p)

# 获取标签内的文本内容
print(body.string)

# 获取标签内的文本内容
print(body.get_text())

# CSS选择器
'''
    1) 标签
    2) id
    3) class
'''
p = soup.select('.board-content')

print(p)

'''
1. 标签选择
2. 方法选择
3. CSS选择
'''

# print(soup.find_all('ul', attrs={'class': 'navbar'}))

subnav = soup.select('.subnav')

'''
节点遍历
    1) 属性
        contents  当前节点的所有直接子节点, 字符串也会被解析成一个独立的节点
        children  当前节点的所有子孙节点. 
    2) 方法
        find
        find_all
        
'''

for child in subnav[0].children:
    print(child)

ls_a = subnav[0].find_all('a')
for a in ls_a:
    print(a)
    print(a.get_text())
    # 访问节点属性
    print(a.attrs.get('onclick'))



