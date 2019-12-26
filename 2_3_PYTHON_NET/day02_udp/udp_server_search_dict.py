from socket import *
ADDR = ("127.0.0.1",8888)
sockfd = socket(AF_INET,SOCK_DGRAM)

sockfd.bind(ADDR)

def search_dict(word):
    f = open("dict.txt", "r")
    for line in f:
        w = line.split()[0]
        if w > word:
            f.close()
            return "Not found"
        elif w == word:
            f.close()
            return line
    else:
        f.close()
        return "Not found"

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
        print("服务端接收数据：", data.decode())

    sockfd.sendto((search_dict(data.decode())).encode(),addr)

sockfd.close()
