"""
Access Token获取

1. 替换
    官网获取的AK：
        API Key ： YbIOzCUWbS4gF7WISYl4xPjG
    官网获取的SK:
        Secret Key : XfcLj3GGmnWGpVNYyR1zO4kXSnytCdPv
2. 运行
    'access_token': '24.4d75d990cc0a330ffcd1edd9d5dc2042.2592000.1578921662.282335-18025715'
"""
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=【官网获取的AK】&client_secret=【官网获取的SK】'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=YbIOzCUWbS4gF7WISYl4xPjG&client_secret=XfcLj3GGmnWGpVNYyR1zO4kXSnytCdPv'
response = requests.get(host)
if response:
    print(response.json())
