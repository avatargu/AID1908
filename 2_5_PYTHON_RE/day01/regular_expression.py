import re

# for item in dir(re):
#     print(item)
#
# print("================================================================")
#
# help(re.findall)
#
# print("================================================================")
#
# help(re.search)
#
# print("================================================================")

# 贪婪
print(re.findall(r"-?[0-9]+","100,-200"))
print(re.findall(r"-{0,1}\d+","100,-200"))
# 非贪婪失效加有效
print(re.findall(r"-??\d+-??","100,-200,300-"))
print(re.findall(r"-*?\d+-*?","100,-200,300-"))

# 空元素(贪婪)
print(re.findall(r"\d*","hello,world."))
print(re.findall(r"\d?","hello,world."))
# 空元素(非贪婪)
print(re.findall(r"\d*?","888"))
print(re.findall(r"\d??","999"))

# 匹配网址
print(re.search(r"(https|http|ftp|file)://\S+","https://www.baidu.com").group()) # 参数默认为0
print(re.search(r"(https|http|ftp|file)://\S+","https://www.baidu.com").group(0)) # 0表示获取整个正则表达式匹配到的内容
print(re.search(r"(https|http|ftp|file)://\S+","https://www.baidu.com").group(1)) # 1表示获取第一个子组匹配到的内容

# 身份证号
print(re.search(r"\d{17}(\d|x)","我的身份证号是：13072119830610053x").group())

# 子组
print(re.search(r"(?P<questions_and_pigs>ab)+","ababab").group())
print(re.search(r"(?P<questions_and_pigs>ab)+","ababab").group("questions_and_pigs"))

# 试验
print(re.findall(r"^hello,world.$","hello,world."))
print(re.findall(r"^hello,world.$","hello,Beijing,hello,world."))
print(re.findall(r"^hello,world.$","hello,world,hello,Beijing."))

