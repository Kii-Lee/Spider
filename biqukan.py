#-*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
url = 'http://www.biqukan.com/1_1094/5403177.html'
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'Cookie':
    'bcolor=; font=; size=; fontcolor=; width=; Hm_lvt_d980a3f9499907d0586dbac4f3207804=1587084623,1587084808; Hm_lpvt_d980a3f9499907d0586dbac4f3207804=1587090954'
}
strhtml = requests.get(url,headers=headers)
# print(strhtml.text.encode(strhtml.encoding).decode('gbk'))
soup = BeautifulSoup(strhtml.text.encode(strhtml.encoding).decode('gbk'),'lxml')
data = soup.find_all('div', class_ = 'showtxt')
# print(data)

for tag in soup.find_all(True):
    print(tag.name)


