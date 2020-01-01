'''
只能在终端执行，不能在Pycharm执行
'''
import getpass # 隐藏输入
import hashlib # 转换加密
print(dir(hashlib))

# 输入隐藏
# pwd = getpass.getpass()
pwd = getpass.getpass("PW:")
print(pwd)


# 三步


# hash对象
# hash = hashlib.md5() # 生成加密对象

# 算法加盐 (#$awv3_)
# abcde12345
# abcde12345#$awv3_
hash = hashlib.md5(("avatargu" + "*#06l_").encode()) # 生成对象

# 对密码进行加密（pwd是你要加密的密码）
hash.update(pwd.encode()) # 算法加密
# 返回加密后的字串
pwd = hash.hexdigest() # 提取加密后的密码
print(pwd)


