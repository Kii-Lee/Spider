import requests
import json
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
FORM_DATA={
    'i': '我爱你',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15870359503290',
    'sign': 'c387ceae2709594581e526348973a323',
    'ts': '1587035950329',
    'bv': '52e219b107829df251d81c3ece9b6c69',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}
headers={
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
response = requests.post(url,data=FORM_DATA,headers=headers)
content = json.loads(response.text)
print(content)
print(content['translateResult'][0][0]['tgt'])