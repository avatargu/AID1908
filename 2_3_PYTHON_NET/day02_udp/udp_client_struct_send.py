from socket import *
import struct
ADDR = ("127.0.0.1",8888)

st = struct.Struct("i16sif")
sockfd = socket(AF_INET,SOCK_DGRAM)

while True:
    id = int(input("id:"))
    if id == 0:
        break
    name = input("name:").encode() # 唯一需要encode()的数据
    age = int(input("age:"))
    score = float(input("score:"))

    data = st.pack(id,name,age,score) # 参数和返回值都是字节串

    sockfd.sendto(data,ADDR)

sockfd.close()
