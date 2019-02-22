'''
selenium
软件测试工具, 功能测试, 单元测试, 性能测试, 压力测试, 安全性测试
1) 安装 selenium
    pip install selenium

2) 浏览器的驱动
    下载驱动程序, 版本
    查看Chrome浏览器的版本

3) 将驱动程序拷贝到项目目录下

注意:
    驱动一般直接放到项目目录下,
    如果不行, 放到Anaconda下的Scripts文件夹下

'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# 打开 浏览器, 获取到浏览器对象
browser = webdriver.Chrome()
# webdriver.Firefox()
# webdriver.Opera()

# 请求URL
url = 'https://www.jd.com/'
browser.get(url)

# 找到页面中的输入框
input = browser.find_element_by_id('key')

# 向输入框中添加字符串
input.send_keys("手机")

# 模拟键盘输入回车
input.send_keys('\n')

# 等待页面
'''
WebDriverWait()
第一个参数: 等待的浏览器对象
第二个参数: 等待的最长时间
'''
wait = WebDriverWait(browser, 10)

# 等待一个操作, 操作类型
# presence_of_element_located(  对象 ) 等待操作
#       等待对象加载完成
#       等待对象的加载, 直到找到对象, 或者超出设置的等待时间
goods_list = wait.until(EC.presence_of_element_located((By.ID, 'J_goodsList')))

print(goods_list)
# 获取手机页面信息
#print(browser.page_source)

# 选择节点的方式
# browser.find_element_by_id()
# browser.find_element_by_class_name()
# browser.find_element_by_css_selector()
div = browser.find_element_by_class_name('gl-i-wrap')

print(div.text)     # 类似于bs4 get_text()
print(div.get_attribute('class'))

ls_li = goods_list.find_elements_by_class_name('gl-item')
print(len(ls_li))

# 在浏览器执行一段JS代码, 让页面滚动到指定位置
browser.execute_script('arguments[0].scrollIntoView();', ls_li[len(ls_li)-1])

# 等待 后面的元素加载完成
time.sleep(1)
ls_li = goods_list.find_elements_by_class_name('gl-item')
print(len(ls_li))

# 遍历60节点, 找到每一个商品的信息
for li in ls_li:
    price = li.find_element_by_css_selector('.p-price i')
    print(price.text)

    name = li.find_element_by_css_selector('.p-name em')
    print(name.text)

time.sleep(100)

# 关闭浏览器对象
browser.close()

