from time import sleep

import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.oculus.com/experiences/quest/"
save_path = "D:\Document\Oculus"

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': save_path, "profile"
                                                                                                ".default_content_setting_values.automatic_downloads": 1}

options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-notifications')
options.add_argument('--no-sandbox')
options.add_argument('--verbose')
options.add_argument('--disable-gpu')
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome()

driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': save_path}}
command_result = driver.execute("send_command", params)
driver.implicitly_wait(30)


def switch_web_pages():
    cur_window = driver.current_window_handle
    all_handles = driver.window_handles
    for ele_handle in all_handles:
        if ele_handle != cur_window:
            driver.switch_to.window(ele_handle)


driver.get(url)
driver.maximize_window()
time.sleep(2)
# driver.find_element_by_id("username").clear()
# driver.find_element_by_id("username").send_keys("13816056177")
# driver.implicitly_wait(5)
# driver.find_element_by_id("userpwd").clear()
# driver.find_element_by_id("userpwd").send_keys("xssxyby198566")
# print("请输入验证码：")
# # 手动输入验证码
# security_code = input()
# time.sleep(1)
# driver.find_element_by_id("imgcode").send_keys(security_code)
# time.sleep(1)
# driver.find_element_by_class_name('form-btn').click()
# driver.implicitly_wait(10)
# # 加一个休眠，这样得到的cookie 才是登录后的cookie,否则可能打印的还是登录前的cookie
# time.sleep(10)
# cookiesAfter = driver.get_cookies()
# len1 = len(cookiesAfter)
# print(len1)
# # 已经知道需要第几个cookie，这里需要第3个cookie，所以选择cookie下标为2
# cookie1 = cookiesAfter[2]
# # 获取当前文件所在路径
# fileNamePath = os.path.split(os.path.realpath(__file__))[0]
# # 拼接config.yaml文件绝对路径
# yamlPath = os.path.join(fileNamePath, 'config.yaml')
# # 以覆盖写入打开文件
# fw = open(yamlPath, 'w', encoding='utf-8')
# # 构建数据
# data = {"cookie1": cookie1}
# # 装载写入yaml文件。
# yaml.dump(data, fw)
#
# wait = WebDriverWait(driver, 10, 0.5)
# wait.until(EC.presence_of_element_located((By.LINK_TEXT, "VIP题库")))
# driver.find_element_by_link_text("VIP题库").click()
# # wait.until(EC.new_window_is_opened(driver.window_handles))
# switch_web_pages()
#
# driver.switch_to.frame('docframe')
#
# wait.until(EC.presence_of_element_located((By.ID, 'folder-list-tree_2_a')))
#
# all_level1_a_list = driver.find_elements_by_class_name('menu-tree-folder')
#
# for ele in all_level1_a_list:
#     print('step1')
#     ele.click()
#     wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.file.folder-box.menu-folder')))
#     sleep(3)
#     all_div_list = driver.find_elements_by_css_selector('.file.folder-box.menu-folder')
#     for fd in all_div_list:
#         print('11')
#         print('fd', fd.text)
#         ActionChains(driver).double_click(fd).perform()
#         sleep(5)
#         all_doc_list = driver.find_elements_by_class_name('filename')
#         for all_ele in all_doc_list:
#             if all_ele.text:
#                 print(all_ele.text)
#                 ActionChains(driver).double_click(all_ele).perform()
#                 sleep(2)
#                 all_file_list = driver.find_elements_by_class_name('filename')
#                 for file in all_file_list:
#                     if file.text:
#                         ActionChains(driver).double_click(file).perform()
#                         sleep(3)
#                         driver.find_element_by_class_name('aui-close').click()
#                         sleep(2)
#                         driver.find_element_by_class_name()(Keys.BACK_SPACE)
# # driver.quit()
