"""
只能在终端运行
不能在PyCharm运行
"""
import getpass

print("==========getpass==========")
for item in dir(getpass):
    print(item)

# 输入隐藏
# password = getpass.getpass()
password = getpass.getpass("password:")

print(password)
