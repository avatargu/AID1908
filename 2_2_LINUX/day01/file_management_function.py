"""
文件管理函数
"""
import os

# 是否存在
print(os.path.exists("dict.txt"))

# 是否文件
print(os.path.isfile("dict.txt"))

# 文件大小
print(os.path.getsize("dict.txt"))

# 文件列表
print(os.listdir("."))

# 删除文件
# print(os.remove("test.txt"))

# 创建目录
# print(os.mkdir("new_directory"))
