import re

def get_address(port):

    file_object = open("exc.txt")

    while True:
        # 每次获取一段内容
        data = ""
        for line in file_object:
            if line == "\n":
                break # 一段结束，退出for循环
            data += line

        # 文件结束退出循环
        if not data:
            break # 全文结束，退出while循环

        match_object_match = re.match(port,data) # 匹配开始位置
        if match_object_match:
            pattern_1 = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}" # 10f3.116c.e6a7
            pattern_2 = r"(\d{1,3}\.){3}\d{1,3}/\d+|Unknown"     # 192.168.100.254/24
            match_object_search_1 = re.search(pattern_1,data) # 匹配第一个内容
            match_object_search_2 = re.search(pattern_2,data) # 匹配第一个内容
            # return match_object_search_1.group()
            return match_object_search_2.group()

    return "没有该端口"

if __name__ == "__main__":
    port = input("端口：")
    print(get_address(port))

































