"""
题目：利用切片操作，实现一个strip()函数，去除字符串的首尾空格
"""
def strip(string = ""):
    # 排除不传参或参数为空字符串的情况
    if string == "":
        return ""

    # 去掉字符串左边的空格
    i = 0
    while True:
        if string[i] == " ":
            i += 1
        else:
            break
    string = string[i:]

    # 去掉字符串右边的空格
    i = -1
    while True:
        if string[i] == " ":
            i -= 1
        else:
            break
    if i != -1:
        string = string[:i + 1]

    # 返回结果字符串
    return string

if __name__ == "__main__":
    # 目标字符串
    string = " hello world "

    # 使用内置字符串方法
    string_stripped = string.strip()
    print(string_stripped)

    # 使用自定义字符串函数
    string_stripped = strip(string)
    print(string_stripped)
