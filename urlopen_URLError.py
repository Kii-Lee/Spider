from urllib import request
from urllib import error
url = 'http://www.iloveyou.com/'
req = request.Request(url)
try:
    response = request.urlopen(req)
    html = response.read.decode('utf-8')
    print(html)
except error.URLError as e:
    print(e.reason)