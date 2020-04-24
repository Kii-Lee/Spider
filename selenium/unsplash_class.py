import time
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
class Unsplash:
    web_url = 'https://unsplash.com/'
    headers = {
        'user-agent':
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
    }
    def scroll_down(self, driver, times):
        for i in range(times):
            print("开始执行第", str(i+1), "次下拉操作")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print("第", str(i+1), "次下拉操作执行完毕")
            print("第", str(i+1), "次等待网页加载...")
            time.sleep(20)
    def get_pic(self):
        print("开始网页get请求")
        driver = webdriver.Chrome()
        driver.get(self.web_url)
        self.scroll_down(driver=driver, times=5)
        print("开始获取所有a标签")
        all_a = BeautifulSoup(driver.page_source, 'lxml').find_all('a', class_='_2Mc8_')
        pic_img_src = []  # 含有图片链接的a标签
        str_max_len = len('<a class="_2Mc8_" href="/photos/V60XQ6u5j7w" itemprop="contentUrl" title="woman in black and white floral long sleeve shirt sitting on white sofa chair"><div class="IEpfq" style="padding-bottom:150%"><img alt="woman in black and white floral long sleeve shirt sitting on white sofa chair" class="_2zEKz" data-perf="eager-loaded-img" data-test="photo-gr')
        for a in all_a:
            if (len(str(a)) > str_max_len):
                pic_img_src.append(a.div.img['src'])
        print("含有图片a标签的数量是：", len(pic_img_src))
        i = 0
        for a in pic_img_src:
            print(a)
            r = requests.get(a, headers=self.headers)
            with open('./imge/img' + str(i) + '.jpg', 'wb') as f:
                f.write(r.content)
                print("第", i, "张图片下载完成！")
                i += 1
unsplash = Unsplash()
unsplash.get_pic()