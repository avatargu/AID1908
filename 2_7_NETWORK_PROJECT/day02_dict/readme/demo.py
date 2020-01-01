while True:
    print("一级界面")
    cmd = input("输入命令：")
    if cmd == "in":
        while True:
            print("二级界面")
            cmd = input("输入命令：")
            if cmd == "out":
                break
