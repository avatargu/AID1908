from socket import *

s = socket()

s.bind(("127.0.0.1",8888))
s.listen(8)
print("Waiting for connection...")
c,addr = s.accept()
print("Connected from",addr)

f = open("picture2.jpg","wb")
while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data)

f.close()
c.close()
s.close()
