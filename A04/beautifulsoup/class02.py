
"""
提取所有猫眼电影.html文件中的电影名与主演
利用for循环来遍历所有文件并打印屏幕
"""

import lxml.html

# 获取etree
etree = lxml.html.etree

print(etree)

# 获取html解析器 - 确定解析的编码
html_parse = etree.HTMLParser(encoding="utf-8")

# 加载html页面

def print_data(n):
    html = etree.parse("猫眼电影{}.html".format(n), html_parse)

    # print(html) # <lxml.etree._ElementTree object at 0x027EC030>

    box = html.xpath("//div[@class='movie-item-info']")

    name = html.xpath("//p[@class='name']/a")

    star = html.xpath("//p[@class='star']")

    for t in name:
        # 获取标签中的内容,去除左右空格
        print(t.text)

    for s in star:
        print(s.text.strip())


for x in range(0 ,10):
    print_data(x)
    print("="*100)

# 先遍历最外层div取出电影名与主演之后再输出出来
# 单独取出时方便导入Excel表格




