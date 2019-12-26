"""
    create database dict character set utf8;
    use dict;
    create table words(id int primary key auto_increment,
                       word char(32),
                       mean text);
"""

import pymysql
import re

f = open("dict.txt")

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="dict",
                     charset="utf8")

cur = db.cursor()

sql = "insert into words (word,mean) values (%s,%s);"

for line in f:
    tup = re.findall(r"(\S+)\s+(.*)",line)[0]  # 获取单词和解释,神奇的正则表达式

    try:
        cur.execute(sql,tup)
        db.commit()
    except:
        db.rollback()

f.close()
cur.close()
db.close()

