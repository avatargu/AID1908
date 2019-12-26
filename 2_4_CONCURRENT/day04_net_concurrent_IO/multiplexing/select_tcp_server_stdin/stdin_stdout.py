import sys

# sys.stdin是标准输入对象
# print(sys.stdin)
# print(type(sys.stdin))

# sys.stdout是标准输出对象
# print(sys.stdout)
# print(type(sys.stdout))

def myinput(string = ""):
    if string:
        print(string,end="")
        sys.stdout.flush()
    string = sys.stdin.readline()
    return string.strip("\n")

print(myinput("请输入："))
