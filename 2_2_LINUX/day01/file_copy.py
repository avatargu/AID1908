# 复制文件
filename = input("Please enter filename:")
try:
    fr = open(filename, "rb")
except FileExistsError as e:
    print(e)
else:
    fw = open("picture_new.jpg", "wb")
    # +++++++++++++++++++++++++++++++++++++++++++++
    # 老师的方法：
    # while True:
    #     data = fr.read(1024) # 1024用来防止文件过大
    #     if not data:
    #         break
    #     fw.write(data)
    # +++++++++++++++++++++++++++++++++++++++++++++
    # ****************
    # 我的方法：
    for line in fr:
        if not line:
            break
        fw.write(line)
    # ****************
    fr.close()
    fw.close()