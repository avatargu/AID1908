"""

"""
from socket import *
import struct
ADDR = ("127.0.0.1",8888)

st = struct.Struct("i16sif")
sockfd = socket(AF_INET,SOCK_DGRAM)
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

sockfd.bind(ADDR)

f = open("student_info.txt","a")
while True:
    try:
        data,addr = sockfd.recvfrom(1024)
    except KeyboardInterrupt:
        print("Server exited")
        break
    except Exception as e:
        print(e)
        continue
    else:
        data = st.unpack(data) # 参数和返回值都是字节串

        id,name,age,score = data

        name = name.decode().strip("\x00") # 唯一需要decode()的数据

        # 文件写入
        student_info = "%-10d %-10s %-10d %.1f\n"%(id,name,age,score)
        f.write(student_info)
        f.flush()

sockfd.close()
