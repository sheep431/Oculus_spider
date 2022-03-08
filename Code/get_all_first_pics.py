from bs4 import BeautifulSoup
import os
import re
html_doc = open(os.path.join(os.getcwd(),'..\\source_html\\all_app.html'),mode='r',encoding="utf8").read()
soup = BeautifulSoup(html_doc,"html.parser")
see_all_lists = soup.find_all(name="a",attrs={"class":"store-section-item-tile"})
for ele in see_all_lists:
    # 封面图片地址
    print(ele.attrs["style"][23:-3])
    # 详情页地址
    print(ele.attrs["href"])
#   开始爬取详情页内容
all_name_lists = soup.find_all(name="div",attrs={"class":"store-section-item__meta-name"})
for ele in all_name_lists:
    # 所有游戏名称
    print(ele.text)
all_price_lists = soup.find_all(name="div",attrs={"class":"store-section-item-byline__price"})
for ele in all_price_lists:
    # 所有游戏价格
    print(ele.text)