import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="teacher",
                     charset="utf8")

cur = db.cursor()

try:
    # 增 =============================================
    name  = input("Name:")
    age   = input("Age:")
    score = input("Score:")
    # sql = "insert into class (name,age,score) values ('%s',%s,%s);"%(name,age,score) # %s加引号
    # cur.execute(sql)
    sql = "insert into class (name,age,score) values (%s,%s,%s);" # %s不加引号
    cur.execute(sql,[name,age,score])

    # 删 =============================================
    sql = "delete from class where score < 60;"
    cur.execute(sql)

    # 改 =============================================
    sql = "update interest set price=11800 where name='Meichangsu';"
    cur.execute(sql)

    db.commit()
except Exception as e:
    db.rollback() # 退回到commit方法执行之前的数据库状态
    print(e)

cur.close()

db.close()

