list01 = ["唐僧","孙悟空","猪八戒","沙僧"]
list02 = [101,102,103,104]
for item in zip(list01,list02):
    print(item)


print("##########################################")


def my_zip(*args):
    length = 0
    # for item in args:
    #     if length < len(item):
    #         length = len(item)
    for i in range(len(min(args,key=lambda item:len(item)))):
        list_target = []
        for element in args:
            list_target.append(element[i])
        yield tuple(list_target)

list01 = ["唐僧","孙悟空","猪八戒","沙僧"]
list02 = [101,102,103,104]
# list03 = ["a","b","c","d"]
# for item in my_zip(list01,list02,list03):
for item in my_zip(list01,list02):
    print(item)






