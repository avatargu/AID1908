1. 创建库(指定字符集)

```
CREATE DATABASE teacher CHARACTER SET UTF8;
```

2. 创建表(指定字符集)

```
CREATE TABLE class(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(32) NOT NULL,
age INT UNSIGNED,
score FLOAT DEFAULT 0.0,
gender ENUM("w","m"),
hobby SET("sing","dance","draw"),
sprint DECIMAL(4,2),
native BIT,
level CHAR,
comment TEXT
);
```

3. 插入表记录(insert)

```
INSERT INTO class VALUES(1,"Meichangsu",18,100.0,"m"),(2,"Nihuangjunzhu",18,90,"w");
INSERT INTO class(name,age,gender) VALUES ("Xiaojingyan",22,"m");
```

```
INSERT INTO interest VALUES(1,"Meichangsu",18,"sing,dance,draw",10.88,1,"A","麒麟才子");
```

4. 删除表记录（delete）

```
DELETE FROM class WHERE name='Qinbanruo';
```

5. 更新表记录(update)

```
UPDATE class SET name="Qinbanruo",age=17 WHERE name='Gongyu';
```

6. 查询表记录(select)

```
SELECT * FROM class where age % 2 = 1;
SELECT name,age FROM class where age % 2 = 1;
```

7. 操作表字段
+ 增加字段(ADD)

> ALTER TABLE 表名 ADD 字段名 数据类型 first;
> ALTER TABLE 表名 ADD 字段名 数据类型 AFTER 字段名;
> ALTER TABLE 表名 ADD 字段名 数据类型;

```
ALTER TABLE class ADD tel CHAR(11) FIRST; # 前
ALTER TABLE class ADD tel CHAR(11) AFTER name; # 中
ALTER TABLE class ADD tel CHAR(11); # 后

ALTER TABLE class ADD tel CHAR(11) NOT NULL;

ALTER TABLE class ADD tel CHAR(11) NOT NULL AFTER name;
```

+ 删除字段(DROP)

> ALTER TABLE 表名 DROP 字段名;

```
ALTER TABLE class DROP tel;

```

+ 修改字段数据类型(MODIFY)

> ALTER TABLE 表名 MODIFY 字段名 新数据类型;

```
ALTER TABLE class MODIFY age TINYINT NOT NULL;

```

+ 修改字段名和数据类型(CHANGE)

> ALTER TABLE 表名 CHANGE 旧字段名 新字段名 新数据类型;

```
ALTER TABLE class CHANGE sex gender ENUM('m','w');

```

+ 重命名表(RENAME)

> ALTER TABLE 表名 RENAME 新表名;

```
ALTER TABLE class RENAME class_1;

```





