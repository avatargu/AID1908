"""
f = open(file_name,access_mode="r",buffering=-1)

    access_mode : r,w,a,+,b
    buffering   : 1表示有行缓冲,默认表示使用系统提供的缓冲机制
===================================================
help(open):
    buffering is an optional integer used to set the buffering policy.
    Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
    line buffering (only usable in text mode), and an integer > 1 to indicate
    the size of a fixed-size chunk buffer.  When no buffering argument is
    given, the default buffering policy works as follows:

    * Binary files are buffered in fixed-size chunks; the size of the buffer
      is chosen using a heuristic trying to determine the underlying device's
      "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
      On many systems, the buffer will typically be 4096 or 8192 bytes long.

    * "Interactive" text files (files for which isatty() returns True)
      use line buffering.  Other text files use the policy described above
      for binary files.
===================================================
缓冲刷新条件：
1. 缓冲区满了
2. 行缓冲换行
3. 程序结束或文件关闭
4. 调用flush()函数
===================================================
read([size])
readline([size])
readlines([size])

write(string)
writelines(string_list)
===================================================
f.tell()
    获取文件偏移量

f.seek(offset[,whence])
    移动文件偏移量位置

    offset
        相对于基准位置移动的字节数,
        负数表示向前移动,
        正数表示向后移动
    whence
        基准位置,
        默认为0,
        0代表从文件开头算起,
        1代表从当前位置算起,
        2代表从文件结尾算起,
        以二进制方式打开文件时,
        基准位置才能是1或2

注意：
1. 以r,w方式打开文件时，文件偏移量在开头
2. 以a方式打开文件时，文件偏移量在结尾
3. 读写操作共用一个文件偏移量
===================================================
f.fileno()
    获取文件描述符
"""

###################################
# # 打开文件try一下
# try:
#     f = open("test", "r")
# except Exception as e:
#     print(e)
###################################
# 读方法不带参数
f = open("test", "r")
data = f.read()
print(data)
f.close()

# 读方法带参数
f = open("test", "r")
while True:
    data = f.read(10)
    if not data:
        break
    print(data)
f.close()

# 推荐的读方法
f = open("test", "r")
for line in f:
    print(line)
f.close()

# with操作自动关闭文件
with open("test","r") as f:
    data = f.read()
    print(data)
###################################
# 缓冲刷新方法1
f = open("test","w",1)
while True:
    data = input(">>")
    if not data:
        break
    f.write(data + "\n")

# 缓冲刷新方法2
f = open("test","w")
while True:
    data = input(">>")
    if not data:
        break
    f.write(data)
    f.flush()
###################################
