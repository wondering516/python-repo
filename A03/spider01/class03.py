import lxml.html

# 获取etree
etree = lxml.html.etree
print(etree) # <module 'lxml.etree' from 'E:\\python\\test_python\\venv\\lib\\site-packages\\lxml\\etree.cp36-win32.pyd'>

# 获取html解析器 - 确定解析的编码
html_parse = etree.HTMLParser(encoding="utf-8")
# 加载html页面
html = etree.parse("猫眼榜单.html",html_parse)
# print(html) # <lxml.etree._ElementTree object at 0x027EC030>

name = html.xpath("//p[@class='name']/a")

star = html.xpath("//p[@class='star']")

for n in name:
    # 获取标签中的内容,去除左右空格
    print(n.text.strip())

for s in star:
    print(s.text.strip())






