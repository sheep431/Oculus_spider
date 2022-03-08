from bs4 import BeautifulSoup
import os
import re
html_doc = open(os.path.join(os.getcwd(),'..\\source_html\\home.html'),mode='r',encoding="utf8").read()
soup = BeautifulSoup(html_doc,"html.parser")
see_all_lists = soup.find_all("a")
href_result_list = []
with open('result_links.txt',mode='w') as f:
    for ele in see_all_lists:
        if ele.get_text() == "See All":
            cur_link = "%s%s"%("https://www.oculus.com/",ele['href'])
            href_result_list.append(cur_link)
            f.writelines("%s\n"%cur_link)
f.close()
