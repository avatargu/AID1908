"""
思路：
将数据库操作类封装，
将tcp_server_dict.py需要的数据库操作分别定义成方法，
在tcp_server_dict.py中实例化对象，
调用方法
"""
import pymysql
import hashlib

SALT = "*#06#" # 盐

class Database:
    def __init__(self,
                 host="localhost",
                 port=3306,
                 user="root",
                 password="123456",
                 charset="utf8",
                 database=None):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset

        self.connect() # 实例化对象自动连接数据库

    # 连接数据库
    def connect(self):
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  password=self.password,
                                  database=self.database,
                                  charset=self.charset)

    # 关闭数据库
    def close(self):
        self.db.close()

    # 创建游标
    def create_cursor(self):
        self.cur = self.db.cursor()

    # 关闭游标
    def close_cursor(self):
        self.cur.close()

    # 加密密码
    def encrypt(self,name,password):
        hash = hashlib.md5((name + SALT).encode())
        hash.update(password.encode())
        return hash.hexdigest()

    # 插入历史记录
    def insert_history(self,name,word):
        sql = "insert into hist (name,word) values (%s,%s)"
        try:
            self.cur.execute(sql,[name,word])
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()

    # 注册处理
    def register(self,name,password):

        # 查看用户是否已经存在
        sql="select * from user where name='%s'"%name
        self.cur.execute(sql)
        record = self.cur.fetchone()
        if record:
            return False

        # 加密密码
        password = self.encrypt(name,password)

        # 增加用户
        sql="insert into user (name,passwd) values (%s,%s)"
        try:
            self.cur.execute(sql,[name,password])
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            self.db.rollback()
            return False

    # 登录处理
    def login(self,name,password):

        # 加密密码
        password = self.encrypt(name,password)

        # 查看用户是否已经注册
        sql = "select * from user where name='%s' and passwd='%s'"%(name,password)
        self.cur.execute(sql)
        record = self.cur.fetchone()
        if record:
            return True
        else:
            return False

    # 查询单词
    def query(self,word):
        sql = "select mean from words where word='%s'"%word
        self.cur.execute(sql)
        record = self.cur.fetchone() # record --> (mean)
        if record:
            return record[0]

    # 历史记录
    def view(self,name):
        sql = "select name,word,time from hist where name='%s' order by time desc limit 10"%name
        self.cur.execute(sql)
        return self.cur.fetchall() # 空元组或元组套元组
