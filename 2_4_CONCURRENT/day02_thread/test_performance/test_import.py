# CPU密集型
def count(x, y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1

# IO密集型
def io():
    write()
    read()

# 阻塞IO
def write():
    f = open("log.txt", "w")
    for i in range(1800000):
        # f.write("Hello,world.\n")
        f.write("0\n")
    f.close()

# 阻塞IO
def read():
    f = open("log.txt")
    lines = f.readlines()
    f.close()
