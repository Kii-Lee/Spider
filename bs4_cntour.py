import requests
from bs4 import BeautifulSoup
import re
url = 'http://www.cntour.cn/'
strhtml = requests.get(url)
soup = BeautifulSoup(strhtml.text,'lxml')
data = soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li > a')
print(data)
for item in data:
    print(item.get_text())
    result={
        'title':item.get_text(),
        'link':item.get('href'),
        'ID':re.findall('\d+',item.get('href'))
    }

print(result)