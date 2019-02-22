from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import traceback

def get_goods_list(browser):
    '获取所有商品列表'

    wait = WebDriverWait(browser, 10)
    ls = []

    count = 0

    while True:
        try:
            goods_list = wait.until(EC.presence_of_element_located((By.ID, 'J_goodsList')))

            ls_li = goods_list.find_elements_by_class_name('gl-item')

            # 在浏览器执行一段JS代码, 让页面滚动到指定位置
            browser.execute_script('arguments[0].scrollIntoView();', ls_li[len(ls_li) - 1])

            time.sleep(1)
            goods_list = wait.until(EC.presence_of_element_located((By.ID, 'J_goodsList')))

            ls_li = goods_list.find_elements_by_class_name('gl-item')


            for li in ls_li:
                goods = {}

                price = li.find_element_by_css_selector('.p-price i').text

                name = li.find_element_by_css_selector('.p-name em').text

                goods['price'] = price
                goods['name'] = name

                ls.append(goods)
                # print(name)

            # 打开下一页
            next = browser.find_element_by_class_name('pn-next')
            js_next = next.get_attribute('onclick')

            if not js_next:
                break

            # 调用页面中的JS 进入下一页
            browser.execute_script(js_next)

            count = 0
        except Exception as e:

            print(repr(e))
            print(traceback.format_exc())

            time.sleep(1)
            count += 1

            if count >= 10:
                return []

    return ls

if __name__ == '__main__':
    browser = webdriver.Chrome()

    browser.get('https://www.jd.com')

    # 用户输入关键字,
    key = input('请输入一个关键字: ')

    # 获取input
    input_markup = browser.find_element_by_id('key')

    input_markup.send_keys(key)
    input_markup.send_keys('\n')

    ls = get_goods_list(browser)

    print(len(ls))
    print(ls)

    # 保存到数据库

    # 提取数据

    # 猿宵节

    '''
    使用selenium
        1) url : https://tieba.baidu.com/index.html
        2) 输入关键字, 搜索该关键字贴吧的所有帖子
        3) 保存到数据库中
    '''


