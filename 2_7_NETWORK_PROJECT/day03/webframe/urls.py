"""
声明客户端能够请求的数据
"""
from views import *

# 路由列表
urls = [
    ("/time",show_time),
    ("/guonei",guonei),
    ("/guoji",guoji)
]
