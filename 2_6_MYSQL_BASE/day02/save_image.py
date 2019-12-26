"""
二进制文件存储

use teacher;
select * from class;
alter table class add image longblob;
"""

import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="teacher",
                     charset="utf8")

cur = db.cursor()

# 图片入库
with open("dilireba.jpeg","rb") as f:
    data = f.read()
try:
    sql = "update class set image = %s where name = 'Qinbanruo';"
    cur.execute(sql,[data])
    db.commit()
except Exception as e:
    db.rollback()
    print(e)

# 图片出库
sql = "select image from class where name='Qinbanruo';"
cur.execute(sql)
data = cur.fetchone()
with open("girlfriend.jpg","wb") as f:
    f.write(data[0])

cur.close()

db.close()

