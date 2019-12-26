import pymysql

# ========================================================
"""
db = pymysql.connect(host     = 主机地址,本地 localhost
                     port     = 端口号,默认 3306
                     user     = 用户名
                     password = 密码
                     database = 数据库
                     charset  = 字符集)
"""
db = pymysql.connect(host     = "localhost",
                     port     = 3306,
                     user     = "root",
                     password = "123456",
                     database = "teacher",
                     charset  = "utf8")

# ========================================================
"""
连接对象(db)的方法:
cur = db.cursor() 创建游标
db.commit()       提交到库
db.rollback()     回滚复原
db.close()        关闭连接
"""
cur = db.cursor()

# ========================================================
"""
游标对象(cur)的方法:
cur.execute(语句,列表/元组) 执行语句
cur.fetchone()        获取第一条数据，返回元组或None
cur.fetchmany(n)      获取前n条数据，返回元组嵌套元组
cur.fetchall()        获取所有数据，返回元组嵌套元组
cur.close()           关闭游标
"""
cur.execute("select * from class where gender='w';")
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

