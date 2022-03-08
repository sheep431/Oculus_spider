import os
import pandas as pd
from Code.get_all_detail_page import get_all_detail_page
import datetime as dt

start_time = dt.datetime.now()
def generate_all_folders(input_file:str,out_path:str):
    if not os.path.exists(input_file):
        return "file:%s does not exist!"
    input_pd = pd.read_excel(input_file)
    global to_override
    to_override = ""
    # for ele in input_pd["标题"].values.tolist():
    passed_num = 0
    for ele in input_pd.iterrows():
        cur_path = os.path.join(out_path,ele[1]['标题'].replace(':',"-").replace("|","-"))
        # 确保创建文件夹
        if not os.path.exists(cur_path):
            os.mkdir(cur_path)
            cur_web = ele[1]["storesectionitemtile_链接"]
            get_all_detail_page(cur_web, cur_path)
        else:
            if "docx" in ",".join(os.listdir(cur_path)):
                passed_num += 1
                print("pass %s generate"%cur_path)
                print("passed num is %s"%passed_num)
            else:
                cur_web = ele[1]["storesectionitemtile_链接"]
                get_all_detail_page(cur_web, cur_path)



    end_time = dt.datetime.now()
    print("All Done in %s min"%((end_time-start_time)/60))
