import requests

def download_videofile(video_links,save_path,names):
    root = save_path
    for link in video_links:
        file_name = names
        print("文件下载:%s" % file_name)
        r = requests.get(link, stream=True)
        with open(root + file_name, 'wb') as f:
            for chunk in r:
                if chunk:
                    f.write(chunk)

        print("%s 下载完成!\n" % file_name)
    print("所有视频下载完成!")
    return