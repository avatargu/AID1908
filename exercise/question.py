import requests
from multiprocessing import *

def text():
    list_ = []
    response = requests.get("https://www.17k.com/list/3063495.html")
    html = response.text
    for line in html.split():
        if "href" in line and 'chapter' in line:
            url=line.split('"')[-2]
            list_.append("www.17k.com"+url)
    return list_

def download(url,num):
    response = requests.get("https://"+url)
    txt = response.content
    with open('./第%d章.html'%num,'wb') as f:
        f.write(txt)

jobs = []
num = 0
for url in text():
    num += 1
    p = Process(target=download,args = (url,num))
    jobs.append(p)
    p.start()
[i.join() for  i in jobs]