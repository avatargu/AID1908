"""
在文件talk.txt中有若干聊天记录
name1:xxxxxx
name2:xxxxxxxx
name1:xxxxxxxxx
name2:xxxxxxx

编写程序把聊天记录按人分开
name1.txt
    xxxxxx
    xxxxxxxxx
name2.txt
    xxxxxxxx
    xxxxxxx
"""
dict_talk = {}

fr = open("talk.txt",'r')
for line in fr:
    if line != '\n':
        name,info = line.split(':',1)
        if name not in dict_talk:
            dict_talk[name] = [info]
        else:
            dict_talk[name].append(info)
fr.close()

for name in dict_talk:
    with open(name+'.txt','w') as fw:
        fw.writelines(dict_talk[name])
