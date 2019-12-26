# 启动和连接MySQL服务

## 服务端启动

```
sudo /etc/init.d/mysql status  
sudo /etc/init.d/mysql start  
sudo /etc/init.d/mysql stop  
sudo /etc/init.d/mysql restart
```

## 客户端连接

* mysql -h主机地址 -u用户名 -p密码

```
mysql -hlocalhost -uroot -p123456
mysql -hlocalhost -uroot -p
```

* 本地连接可以省略 -h 选项

```
mysql -uroot -p123456
mysql -uroot -p
```

## 清屏

`ctrl + l`

## 关闭连接

```
ctrl + d  
exit
```
