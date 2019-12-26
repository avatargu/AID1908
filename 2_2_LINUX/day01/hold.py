"""
空洞文件
"""
f = open("log.txt","wb")

f.write(b"start")
f.seek(1024*1024,2)
f.write(b"end")

f.close()