import requests
from bs4 import BeautifulSoup
import os
url = "https://unsplash.com"
headers = {
'user-agent':
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
}
strhtml = requests.get(url,headers=headers)
# print(strhtml.text)
soup = BeautifulSoup(strhtml.text, 'lxml')
all_a = soup.find_all('a', class_="_2Mc8_")
pic_img_src = []#含有图片链接的a标签
str_max_len = len('<a class="_2Mc8_" href="/photos/V60XQ6u5j7w" itemprop="contentUrl" title="woman in black and white floral long sleeve shirt sitting on white sofa chair"><div class="IEpfq" style="padding-bottom:150%"><img alt="woman in black and white floral long sleeve shirt sitting on white sofa chair" class="_2zEKz" data-perf="eager-loaded-img" data-test="photo-gr')
for a in all_a:
    if(len(str(a))>str_max_len):
        pic_img_src.append(a.div.img['src'])
i = 0
for a in pic_img_src:
    print(a)
    r = requests.get(a,headers=headers)
    with open('./imge/img'+str(i)+'.jpg', 'wb') as f:
        f.write(r.content)
        print("第",i,"张图片下载完成！")
        i += 1
