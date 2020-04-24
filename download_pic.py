import os
import requests
headers = {
'user-agent':
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
}
r = requests.get('https://images.unsplash.com/photo-1586984479324-ec660ceb03c0?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=crop&amp;w=300&amp;q=60',headers=headers)
with open('./imge/img9.jpg','wb') as f:
    f.write(r.content)