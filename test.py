import requests
from bs4 import BeautifulSoup

url = "https://www.bilibili.com/video/BV1qW4y1a7fU/?p=61&spm_id_from=pageDriver&vd_source=16614f0155ab54f92a8ceafa025bb440"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 找到包含视频信息的div元素  
video_div = soup.find("div", class_="video-info")

# 提取摘要信息  
summary = video_div.find("div", class_="video-abstract").text.strip()

# 打印摘要  
print(summary)