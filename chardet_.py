import requests
import chardet
url = 'http://www.baidu.com'
strhtml = requests.get(url)
# print(strhtml.text)
print(type(strhtml))
charset = chardet.detect(strhtml.text.encode())
print(charset)