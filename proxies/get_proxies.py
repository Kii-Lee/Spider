#_*_coding:utf-8_*_
import requests
import json
from bs4 import BeautifulSoup
class GetIP(object):
    def __init__(self):
        self.url = 'https://www.xicidaili.com/nn/'
        self.check_url='https://www.ip.cn'
        self.ip_list=[]
    @staticmethod
    def get_html(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
        }
        try:
            strhtml = requests.get(url, headers=headers)
            strhtml.encoding = 'utf-8'
            return strhtml.text
        except Exception as e:
            print('exception occured')
            return ''
    def get_available_ip(self, ip_address, ip_port):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
        }
        ip_url_next = '://'+ip_address+':'+ip_port
        proxies = {'http':'http'+ip_url_next, 'https':'https'+ip_url_next}
        try:
            r = requests.get(self.check_url, headers=headers, proxies=proxies, timeout=3)
            html = r.text
        except:
            print('fail-%s'%ip_address)
        else:
            print('success-%s'%ip_address)
            soup = BeautifulSoup(html, 'lxml')
            div = soup.find(class_='well')
            if div:
                print(div.text)
            ip_info = {'address':ip_address, 'port':ip_port}
            self.ip_list.append(ip_info)
    def main(self):
        web_html = self.get_html(self.url)
        soup = BeautifulSoup(web_html, 'lxml')
        ip_list = soup.find(id='ip_list').find_all('tr')
        for ip_info in ip_list:
            td_list = ip_info.find_all('td')
            if len(td_list) > 0:
                ip_address = td_list[1].text
                ip_port = td_list[2].text
                self.get_available_ip(ip_address,ip_port)
            with open('./ip.txt', 'w') as file:
                json.dump(self.ip_list, file)
            print(self.ip_list)
if __name__ == '__main__':
    get_ip = GetIP()
    get_ip.main()