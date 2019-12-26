"""
pymysql读流程：
1. 创建连接 db = pymysql.connect(...)
2. 创建游标 cur = db.cursor()
3. 执行语句 cur.execute("select ...")
4. 获取数据 cur.fetchone()/cur.fetchmany(n)/cur.fetchall()
5. 关闭游标 cur.close()
6. 关闭连接 db.close()

pymysql写流程：
1. 创建连接 db = pymysql.connect(...)
2. 创建游标 cur = db.cursor()
3. 执行语句 cur.execute("insert/delete/update ...")
4. 提交到库 db.commit()
5. 关闭游标 cur.close()
6. 关闭连接 db.close()
"""

import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="teacher",
                     charset="utf8")

cur = db.cursor()

sql = "select * from class where gender='w';"
cur.execute(sql)

one_row = cur.fetchone()
print(one_row)
print(one_row[0])
many_row = cur.fetchmany(2)
print(many_row)
print(many_row[0])
all_row = cur.fetchall()
print(all_row)
print(all_row[0])

cur.close()

db.close()

"""
pymysql读流程：
1. 创建连接 db = pymysql.connect(...)
2. 创建游标 cur = db.cursor()
3. 执行语句 cur.execute("select ...")
4. 获取数据 cur.fetchone()/cur.fetchmany(n)/cur.fetchall()
5. 关闭游标 cur.close()
6. 关闭连接 db.close()

pymysql写流程：
1. 创建连接 db = pymysql.connect(...)
2. 创建游标 cur = db.cursor()
3. 执行语句 cur.execute("insert/delete/update ...")
4. 提交到库 db.commit()
5. 关闭游标 cur.close()
6. 关闭连接 db.close()
"""

import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="teacher",
                     charset="utf8")

cur = db.cursor()

sql = "insert into class values (1,'梅长苏',17,99.9,'m','2019-2-19');"
cur.execute(sql)

db.commit()

cur.close()

db.close()

