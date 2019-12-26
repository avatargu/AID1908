"""
百度智能云

1. 替换
    本地文件: tiger.jpg
    'access_token': '24.4d75d990cc0a330ffcd1edd9d5dc2042.2592000.1578921662.282335-18025715'
2. 运行
    {'score': '0.822527', 'name': '西伯利亚虎'}
"""
import requests
import base64

'''
动物识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
# 二进制方式打开图片文件
# f = open('[本地文件]', 'rb')
f = open('tiger.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
# access_token = '[调用鉴权接口获取的token]'
access_token = '24.4d75d990cc0a330ffcd1edd9d5dc2042.2592000.1578921662.282335-18025715'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())
