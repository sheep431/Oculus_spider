from bs4 import BeautifulSoup
import os
import re
html_doc = open(os.path.join(os.getcwd(),'..\\source_html\\home.html'),mode='r').read()
soup = BeautifulSoup(html_doc,"html.parser")
see_all_lists = soup.find_all("a")
href_result_list = []
for ele in see_all_lists:
    if ele.get_text() == "See All":
        href_result_list.append(ele['href'])
print(href_result_list)