import os
from bs4 import BeautifulSoup
import pandas as pd
from Code.bulk_download import bulk_download
import datetime as dt
# import pyautogui

def get_all_details(out_path:str,mode:str):
        if mode=="hdris":
                # 获得网页内容
                soup = BeautifulSoup(open("source_html/poly_heaven_HDRIS.html",encoding='utf8'),features="lxml")
                # print(soup)
                # 获得所有a link
                a_link_list = soup.find_all("a", attrs={"class": "GridItem_gridItem__0cuEz"})
                list_title = []
                list_csdn_title = []
                list_desc = []
                list_page_link = []
                list_download_link = []
                list_img_link = []
                for ele in a_link_list[:1]:
                        cur_resource_title = str(ele["href"]).split("/")[2]
                        cur_csdn_title = "%s_游戏开发_VR开发_天空盒子_天空背景_无水印_unitySkybox_高清图片资源_16K_EXR"%cur_resource_title
                        cur_desc = "可用于UnityVR开发，3D游戏开发，高清天空盒子Skybox素材，游戏环境背景素材，无水印。使用方法：1-导入Unity后将图片的Shape转换成cube形式，2-创建空Material，并转换成Cube/skybox形式，3-将图片拖入新建的SkyboxMaterial，4-用刚创建的Material代替项目中原本的系统默认Skybox"
                        cur_detail_page_link = "https://polyhaven.com"+ele["href"]
                        cur_download_link = "https://dl.polyhaven.org/file/ph-assets/HDRIs/exr/16k%2B/"+cur_resource_title+"_16k.exr"
                        if len(ele.find_all("img")) > 1:
                                cur_img_link = ele.find_all("img")[1]["src"]
                        else:
                                cur_img_link = "No img link"
                        list_title.append(cur_resource_title)
                        list_csdn_title.append(cur_csdn_title)
                        list_desc.append(cur_desc)
                        list_page_link.append(cur_detail_page_link)
                        list_download_link.append(cur_download_link)
                        list_img_link.append(cur_img_link)
                df_result = pd.DataFrame()
                df_result["title"] = list_title
                df_result["csdn_title"] = list_csdn_title
                df_result["desc"] = list_desc
                df_result["page_link"] = list_page_link
                df_result["download_link"] = list_download_link
                df_result["img_link"] = list_img_link

                bulk_download(df_result["download_link"].to_list(),"exr",r"E:\toCSDN\polyHeaven\hdris")
        if mode=="textures":
                # 获得网页内容
                soup = BeautifulSoup(open("source_html/poly_heaven_textures.html", encoding='utf8'), features="lxml")
                # print(soup)
                # 获得所有a link
                a_link_list = soup.find_all("a", attrs={"class": "GridItem_gridItem__0cuEz"})
                list_title = []
                list_csdn_title = []
                list_desc = []
                list_page_link = []
                list_download_link = []
                list_img_link = []
                for ele in a_link_list[:1]:
                        cur_resource_title = str(ele["href"]).split("/")[2]
                        cur_csdn_title = "%s_游戏开发_VR开发_texture_纹理贴图_unity_高清游戏素材_8K_Blender直接导入" % cur_resource_title
                        cur_desc = "可用于UnityVR开发，3D游戏开发，高清天空盒子Skybox素材，游戏环境背景素材，无水印。使用方法：1-导入Unity后将图片的Shape转换成cube形式，2-创建空Material，并转换成Cube/skybox形式，3-将图片拖入新建的SkyboxMaterial，4-用刚创建的Material代替项目中原本的系统默认Skybox"
                        cur_detail_page_link = "https://polyhaven.com" + ele["href"]
                        cur_download_link = r"https://polyhaven.com/__download__/%s/%s_8k.blend.zip"%(dt.datetime.strftime(dt.datetime.utcnow(),"%Y%m%d%H%M%S"),cur_resource_title)
                        print(cur_download_link)
                        return "done"
                        if len(ele.find_all("img")) > 1:
                                cur_img_link = ele.find_all("img")[1]["src"]
                        else:
                                cur_img_link = "No img link"
                        list_title.append(cur_resource_title)
                        list_csdn_title.append(cur_csdn_title)
                        list_desc.append(cur_desc)
                        list_page_link.append(cur_detail_page_link)
                        list_download_link.append(cur_download_link)
                        list_img_link.append(cur_img_link)
                df_result = pd.DataFrame()
                df_result["title"] = list_title
                df_result["csdn_title"] = list_csdn_title
                df_result["desc"] = list_desc
                df_result["page_link"] = list_page_link
                df_result["download_link"] = list_download_link
                df_result["img_link"] = list_img_link

                bulk_download(df_result["download_link"].to_list(), "exr", r"E:\toCSDN\polyHeaven\hdris")