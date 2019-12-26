from socket import *

s = socket()

s.connect(("127.0.0.1",8888))

f = open("picture.jpg","rb")
# 我的方法：
# for data in f:
#     if not data:
#         break
#     s.send(data)
# 祁老师的方法：
while True:
    data = f.read(1024)
    if not data:
        break
    s.send(data)

f.close()
s.close()





