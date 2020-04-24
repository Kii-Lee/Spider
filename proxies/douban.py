#_*_coding:utf-8_*_
from bs4 import BeautifulSoup
import datetime
import requests
import json
import random

ip_random = -1
article_tag_list = []
article_type_list = []
def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
    }
    global ip_random
    ip_rand, proxies = get_proxy(ip_random)
    print(proxies)
    try:
        request = requests.get(url, headers=headers, proxies=proxies, timeout=3)
    except:
        request_status = 500
    else:
        request_status = request.status_codes
    print(request_status)
    while request_status != 200:
        ip_random = -1
        ip_rand, proxies = get_proxy(ip_random)
        print(proxies)
        try:
            request = requests.get(url=url, headers=headers, proxies=proxies, timeout=3)
        except:
            request_status = 500
        else:
            request_status = request.status_code
        print(request_status)
    ip_random = ip_rand
    request.encoding = 'gbk'
    html = request.content
    print(html)
    return html
def get_proxy(random_number):
    with open('ip.txt', 'r') as file:
        ip_list = json.load(file)
        if random_number == -1:
            random_number = random.randint(0, len(ip_list)-1)
        ip_info = ip_list[random_number]
        ip_url_next = '://'+ip_info['address']+':'+ip_info['port']
        proxies = {'http':'http'+ip_url_next, 'https':'https'+ip_url_next}
        return random_number, proxies
if __name__ == '__main__':
    start_time = datetime.datetime.now()
    url = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
    base_url = 'http://book.douban.com/tag/'
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    article_tag_list = soup.find_all(class_='tag-title-wrapper')
    tagCol_list = soup.find_all(class_='tagCol')
    for table in tagCol_list:
        sub_type_list = []
        a = table.find_all['a']
        for book_type in a:
            sub_type_list.append(book_type.text)
        article_type_list.append(sub_type_list)
    for sub in article_type_list:
        for sub1 in sub:
            title = '========'+sub1+'========'
            print(title)
            print(base_url+sub1+'?start=0'+'&type=S')
            with open('book.txt','a',encoding='utf-8') as f:
                f.write('\n'+title+'\n')
                f.write(url+'\n')
            for start in range(0,2):
                url = base_url+sub1+'?start=%s'%(start*20)+'&type=S'
                html = get_html(url)
                soup = BeautifulSoup(html, 'lxml')
                li = soup.find_all(class_='subject-item')
                for div in li:
                    info = div.find(class_='info').find('a')
                    img = div.find(class_='pic').find('img')
                    content = '书名：<%s>'%info['title']+'书本图片'+img['src']+'\n'
                    print(content)
                    with open('book.txt','a',encoding='utf-8') as f:
                        f.write(content)
end_time = datetime.datetime.now()
print('耗时：',(end_time-start_time).seconds)
