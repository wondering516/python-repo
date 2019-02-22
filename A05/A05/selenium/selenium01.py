from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def get_goods_list():
    '获取所有商品列表'
    wait =time.sleep(10)
    good_list = wait.until(EC.presence_of_all_elements_located((By.Id, 'J_goodList')))
    ls_li = good_list.find_element_byclass_name('gl_item')

    ls = []

    for li in ls_li:
        goods = {}

        price = ls
    pass



if __name_=='__main__':
    browser = webdriver.Chrome

    browser.get("http://wwww.jd.com/")

    key =input("请输入一个关键字: ")

    input