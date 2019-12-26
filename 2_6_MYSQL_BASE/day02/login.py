"""
注册,登录：
use teacher;
create table user(id int primary key auto_increment,
                  name varchar(32) not null,
                  password varchar(32) not null);
"""

import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="teacher",
                     charset="utf8")

cur = db.cursor()

def register():
    name = input("用户名：")
    password = input("密码：")
    # 判断用户名是否重复
    sql = "select * from user where name='%s'"%name
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return False
    try:
        sql = "insert into user (name,password) values (%s,%s)"
        cur.execute(sql,[name,password])
        db.commit()
        return True
    except:
        db.rollback()
        return False

def login():
    name = input("用户名：")
    password = input("密码：")
    # 判断用户名和密码组合是否存在
    sql = "select * from user where name='%s' and password = '%s'"%(name,password)
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return True

while True:
    print("""
        ============
        1.注册 2.登录
        ============
    """)
    cmd = input("请输入命令(1或2)：")
    if cmd == "1":
        if register():
            print("注册成功")
        else:
            print("注册失败")
    elif cmd == "2":
        if login():
            print("登录成功")
            break
        else:
            print("登录失败")
    else:
        print("命令错误")

cur.close()
db.close()

