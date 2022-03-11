from selenium import webdriver
from time import sleep

def click_each_page(page_list:list,out_path:str,params:list):
    for ele in page_list:
        # 先用selenium点开视频和介绍
        save_path = out_path

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
        driver.get(ele)
        driver.maximize_window()

        # 开始定位和操作
        download_ele = driver.find_element_by_class_name("Download_downloadBtnWrapper__uIC9x")
        download_ele.click()
        sleep(100)
