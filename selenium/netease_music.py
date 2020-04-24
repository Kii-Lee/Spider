import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
class AlbumCover:
    init_url = 'https://music.163.com/#/artist/album?id=101988&limit=12&offset='
    headers = {
        'user-agent':
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
    }
    def save_img(self, url, file_name):
        print('开始请求图片地址，过程会有点长...')
        img = requests.get(url, headers=self.headers)
        with open('./album/'+file_name, 'wb') as f:
            f.write(img.content)
        print('图片保存完成')
    def spider(self):
        print('start')
        driver = webdriver.Chrome()
        for i in range(0,133,12):
            driver.get(self.init_url+str(i))
            driver.switch_to.frame('g_iframe')
            html = driver.page_source
            # print(html)
            soup = BeautifulSoup(html, 'lxml')
            all_li = soup.find(id='m-song-module').find_all('li')
            for li in all_li:
                img_name = li.p['title'].replace('/',' ').replace(':',',')+'.jpg'
                end_pos = li.div.img['src'].index('?')
                img_url = li.div.img['src'][:end_pos]
                # print(img_name,':',img_url)
                self.save_img(img_url, img_name)
album = AlbumCover()
album.spider()