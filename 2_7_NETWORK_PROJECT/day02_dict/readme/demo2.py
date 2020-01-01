"""
只能在终端运行
不能在PyCharm运行
"""
import getpass # 隐藏
import hashlib # 加密

print("==========getpass==========")
for item in dir(getpass):
    print(item)

print("==========hashlib==========")
for item in dir(hashlib):
    print(item)

# 输入隐藏
# password = getpass.getpass()
password = getpass.getpass("password:")
print(password)

# 三步加密

# 第一步：对象
# hash = hashlib.md5()
hash = hashlib.md5(("avatargu" + "*#06#").encode()) # 加盐

# 第二步：加密
hash.update(password.encode())

# 第三步：提取
password = hash.hexdigest()

print(password)
