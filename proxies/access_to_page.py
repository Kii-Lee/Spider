import requests
from bs4 import BeautifulSoup
url = 'https://www.xicidaili.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
}
try:
    strhtml = requests.get(url, headers=headers)
    # request.encoding = 'utf-8'
except Exception as e:
    print('exception occured')
# print(strhtml.text)
soup = BeautifulSoup(strhtml.text, 'lxml')
ip_list = soup.find(id='ip_list').find_all('tr')
# print(tr_list)
for ip_info in ip_list:
    td_list = ip_info.find_all('td')
    if len(td_list) > 0:
        ip_address = td_list[1].text
        ip_port = td_list[2].text
        print(ip_address+':'+ip_port)